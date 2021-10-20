from logging import error
import requests
from requests import status_codes
import swagger_client as sw
import json
import pandas

class Project():
    def __init__(self, project, access_token, host=None, ssl=True):
        self.project = project.strip('/')
        s = self.project.split("/")
        if len(s) != 3:
            raise ValueError('invalid project')
        else:
            self.host = s[0]
            self.team_id = s[1]
            self.project_id = s[2]

        self.project = project
        self.access_token = access_token

        cfg = sw.Configuration()
        #cfg.api_key["token"] = access_token
        
        scheme = "https://" if ssl else "http://"
        cfg.host = scheme + (self.host if host is None else host) + "/api/v1"

        self.sw_client = sw.ApiClient(cfg, "Authorization", "Bearer "+access_token)

    def table(self, table_name):
        return Table(self.team_id, self.project_id, table_name, self.sw_client, self.access_token)

    def list_tables(self):
        return self.table(None).list()

class Table():
    def __init__(self, team_id, project_id, table_name, sw_client, token=None):
        self.team_id = team_id
        self.project_id = project_id
        self.table_name = table_name
        self.sw_client = sw_client
        self.api = sw.TablesApi(self.sw_client)
        self.token = token

    def list(self):
        return self.api.list_tables(self.team_id, self.project_id)

    def get(self, get_schema=False):
        t = None
        try:
            self.api.get_table(self.team_id, self.project_id, self.table_name, schema=get_schema)
        except sw.rest.ApiException as e:
            if(e.status != 404):
                raise e
        return t

    def exists(self):
        return self.get() is not None
        
    def create(self):
        self.api.update_table(self.team_id, self.project_id, self.table_name)

    def delete(self):
        self.api.delete_table(self.team_id, self.project_id, self.table_name)

    def update(self, prop, value):
        action = sw.PatchAction(action="UPDATE", _property=prop, value=value)
        self.api.update_table_property(self.team_id, self.project_id, self.table_name, body=action)

    def update_schema(self, schema):
        self.update("schema", json.dumps(schema));
        
    def put(self, data, file_name=None, tag=None, content_type=None):
        if file_name is None or file_name.strip() == "":
            file_name = "0"
        if tag is None:
            tag = ""
        if content_type is None or content_type.strip() == "":
            content_type = ""

        self.api.put_table_data_file(self.team_id, self.project_id, self.table_name, file_name , x_di_tag=tag, content_type=content_type, body=data)

    def put_csv(self, df, file_name=None, tag=None):
        body = df.to_csv()
        self.put(body, file_name, tag, "text/csv")
        
    def put_parquet(self, df, file_name=None, tag=None):
        body = df.to_parquet()
        self.put(body, file_name, tag, "application/parquet")

    def files(self):
        return self.api.list_table_data_files(self.team_id, self.project_id, self.table_name)

    def get_file_meta(self, data_file_name):
        return self.api.get_table_data_file_meta(self.team_id, self.project_id, self.table_name, data_file_name)

    def _get_file_url(self, file_name):
        url = '/'.join([self.sw_client.configuration.host, "teams", self.team_id, "projects", self.project_id, "tables", self.table_name, "data", file_name])
        if self.token:
            url += "?token=" + self.token

        r = requests.get(url, allow_redirects=False)
        if r.status_code == 303:
            return r.headers.get('Location')
        else:
            raise BaseException("Get DataFile content failed: %s" % str(r.status_code))
    
    def _read_df(self, file_name, format):
        url = self._get_file_url(file_name)
        if url and format == "text/csv":
            return pandas.read_csv(url)
        elif format == "application/parquet":
            return pandas.read_parquet(url)
        else:
            raise BaseException("File format unsupported.")

    def read(self):
        dfs = []
        files = self.files()
        for f in files:
            df = self._read_df(f.name, f.content_type)
            dfs.append(df)
        return pandas.concat(dfs)
        
def schema(df):
    columns = []
    for name in df.index.names:
        columns.append({
            "name": name,
            "data_type": str(df.index.dtype),
            "key": "index"
        })
    for index, value in df.dtypes.items():
        columns.append({
            "name": index,
            "data_type": str(value)
        })
    return {"columns": columns}

def _parse_identity(identity):
    s = identity.strip().split('/')
    if len(s) != 4:
        raise ValueError('invalid identity, it shold be like 42di.cn/your_id/your_project/your_table')
    project_id = '/'.join(s[:-1])
    table_name = s[-1:][0]
    return (project_id, table_name)

def put(identity, df, token, create_table=True, update_schema=False):
    project_id, table_name = _parse_identity(identity)
    project = Project(project_id, token)

    table = project.table(table_name)
    if not table.exists() and create_table:
        table.create()

    table.put_parquet(df)

    if update_schema:
        table.update_schema(schema(df))

def read(identity, token):
    project_id, table_name = _parse_identity(identity)
    project = Project(project_id, token)
    return project.table(table_name).read()