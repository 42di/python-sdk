from logging import error
import requests
from requests import status_codes
import swagger_client as sw
import json
import pandas
import warnings
from enum import Enum

#warnings.filterwarnings('default')

SSL = True
TOKEN = None

class ResourceType(Enum):
    INVALID = 0
    TEAM = 1
    PROJECT = 2
    DATASET = 3
    FILE = 4

class ResourceId():
    def __init__(self, uri):
        self.endpoint = None
        self.team_id = None
        self.project_id = None
        self.dataset_id = None
        self.file_name = None

        self._parse_uri(uri)

    def _parse_uri(self, uri):
        if not uri:
            return

        s = uri.strip().split('/')
        length = len(s)

        if length < 1 or length > 5:
            raise ValueError("invalid ResourceId: %s" % uri)

        if length > 0:
            self.endpoint = s[0]
        if length > 1:
            self.team_id = s[1]
        if length > 2:
            self.project_id = s[2]
        if length > 3:
            self.dataset_id = s[3]
        if length > 4:
            self.file_name = s[4]

    def resource_type(self):
        if self.file_name:
            return ResourceType.FILE
        elif self.dataset_id:
            return ResourceType.DATASET
        elif self.project_id:
            return ResourceType.PROJECT
        elif self.team_id:
            return ResourceType.TEAM
        else:
            return ResourceType.INVALID

    def team_resource_id(self):
        if self.endpoint and self.team_id:
            return '/'.join([self.endpoint, self.team_id])
        else:
            return None

    def project_resource_id(self):
        if self.endpoint and self.team_id and self.project_id:
            return '/'.join([self.endpoint, self.team_id, self.project_id])
        else:
            return None

    def dataset_resource_id(self):
        if self.endpoint and self.team_id and self.project_id and self.dataset_id:
            return '/'.join([self.endpoint, self.team_id, self.project_id, self.dataset_id])
        else:
            return None

    def file_resource_id(self):
        if self.endpoint and self.team_id and self.project_id and self.dataset_id and self.file_name:
            return '/'.join([self.endpoint, self.team_id, self.project_id, self.dataset_id, self.file_name])
        else:
            return None

    def __str__(self):
        resource_type = self.resource_type()
        if resource_type == ResourceType.TEAM:
            return self.team_resource_id()
        elif resource_type == ResourceType.PROJECT:
            return self.project_resource_id()
        elif resource_type == ResourceType.DATASET:
            return self.dataset_resource_id()
        elif resource_type == ResourceType.FILE:
            return self.file_resource_id()
        else:
            return None

    def str(self):
        return self.__str__()

def _create_sw_client(host, token):
    cfg = sw.Configuration()
    #cfg.api_key["token"] = token
    scheme = "https://" if SSL else "http://"
    cfg.host = scheme + host + "/api/v1"

    return sw.ApiClient(cfg, "Authorization", "Bearer " + token)

class Project():
    def __init__(self, project, access_token=None):
        global SSL
        global TOKEN

        ri = ResourceId(project)
        if not ri.project_resource_id():
            raise ValueError("invalid project resource identity: %s" % project)

        self.host = ri.endpoint
        self.team_id = ri.team_id
        self.project_id = ri.project_id

        self.access_token = access_token

        if not self.access_token:
            self.access_token = TOKEN

        if not self.access_token:
            raise ValueError("access token required.")

        self.sw_client = _create_sw_client(self.host, self.access_token)

    def dataset(self, dataset_id):
        return Dataset(self.team_id, self.project_id, dataset_id, self.sw_client, self.access_token)

    def list_datasets(self):
        return self.dataset(None).list()
    
    # Deprecated
    def table(self, table_name):
        warnings.warn("Deprecated, use dataset instead.", DeprecationWarning)
        return self.dataset(table_name)

    def list_tables(self):
        warnings.warn("Deprecated, use list_datasets instead.", DeprecationWarning)
        return self.list_datasets()


class Dataset():
    def __init__(self, team_id, project_id, dataset_id, sw_client, token=None):
        self.team_id = team_id
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.sw_client = sw_client
        self.api = sw.DatasetsApi(self.sw_client)
        self.token = token

    def list(self):
        try:
            return self.api.list_datasets(self.team_id, self.project_id)
        except sw.rest.ApiException as e:
            _err_format(e)

    def get(self, get_schema=False):
        t = None
        try:
            t = self.api.get_dataset(self.team_id, self.project_id, self.dataset_id, schema=get_schema)
        except sw.rest.ApiException as e:
            if e.status != 404:
                _err_format(e)
        return t

    def exists(self):
        return self.get() is not None
        
    def create(self):
        try:
            self.api.update_dataset(self.team_id, self.project_id, self.dataset_id)
        except sw.rest.ApiException as e:
            _err_format(e)

    def delete(self):
        try:
            self.api.delete_dataset(self.team_id, self.project_id, self.dataset_id)
        except sw.rest.ApiException as e:
            _err_format(e)

    def update(self, prop, value):
        action = sw.PatchAction(action="UPDATE", _property=prop, value=value)
        try:
            self.api.update_dataset_property(self.team_id, self.project_id, self.dataset_id, body=action)
        except sw.rest.ApiException as e:
            _err_format(e)

    def update_schema(self, schema):
        self.update("schema", json.dumps(schema));
        
    def put(self, data, file_name=None, tag=None, content_type=None):
        if file_name is None or file_name.strip() == "":
            file_name = "0"
        if tag is None:
            tag = ""
        if content_type is None or content_type.strip() == "":
            content_type = ""
        try:
            self.api.put_dataset_data_file(self.team_id, self.project_id, self.dataset_id, file_name , x_di_tag=tag, content_type=content_type, body=data)
        except sw.rest.ApiException as e:
            _err_format(e)

    def put_csv(self, df, file_name=None, tag=None):
        body = df.to_csv()
        self.put(body, file_name, tag, "text/csv")
        
    def put_parquet(self, df, file_name=None, tag=None):
        body = df.to_parquet()
        self.put(body, file_name, tag, "application/parquet")

    def files(self):
        try:
            return self.api.list_dataset_data_files(self.team_id, self.project_id, self.dataset_id)
        except sw.rest.ApiException as e:
            _err_format(e)

    def get_file_meta(self, data_file_name):
        try:
            return self.api.get_dataset_data_file_meta(self.team_id, self.project_id, self.dataset_id, data_file_name)
        except sw.rest.ApiException as e:
            _err_format(e)

    def _get_file_url(self, file_name):
        url = '/'.join([self.sw_client.configuration.host, "teams", self.team_id, "projects", self.project_id, "datasets", self.dataset_id, "data", file_name])
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

    def read(self, file_name=[]):
        filters = set(file_name)

        dfs = []
        files = self.files()
        for f in files:
            if len(file_name) > 0 and f.name not in filters:
                continue
            df = self._read_df(f.name, f.content_type)
            dfs.append(df)
        return None if len(dfs) == 0 else pandas.concat(dfs)
        
def Table(Dataset):
    def __init__(self, team_id, project_id, table_name, sw_client, token=None):
        Dataset.__init__(team_id, project_id, table_name, sw_client, token)
        warnings.warn("Deprecated, use Dataset instead.", DeprecationWarning)

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

def dataset(identity, token=None):
    ri = ResourceId(str(identity))
    if ri.resource_type() != ResourceType.DATASET:
        raise ValueError("invalid resource id: %s" % identity)

    return Project(ri.project_resource_id(), access_token=token).dataset(ri.dataset_id)

def put(identity, data, token=None, content_type='application/parquet', create=True, update_schema=False):
    ri = ResourceId(str(identity))
    if ri.resource_type() != ResourceType.DATASET and ri.resource_type() != ResourceType.FILE:
        raise ValueError("invalid resource id: %s" % identity)

    project = Project(ri.project_resource_id(), token)
    
    dataset = project.dataset(ri.dataset_id)
    if not dataset.exists() and create:
        dataset.create()

    if content_type == 'text/csv':
        dataset.put_csv(data, ri.file_name)
    elif content_type == 'application/parquet':
        dataset.put_parquet(data, ri.file_name)
    else:
        dataset.put(data, file_name=ri.file_name, tag=None, content_type=content_type)

    if update_schema:
        dataset.update_schema(schema(data))

def read(identity, token=None):
    ri = ResourceId(str(identity))
    if ri.resource_type() != ResourceType.DATASET and ri.resource_type() != ResourceType.FILE:
        raise ValueError("invalid resource id: %s" % identity)

    project = Project(ri.project_resource_id(), token)
    files = []
    if ri.file_name:
        files.append(ri.file_name)

    return project.dataset(ri.dataset_id).read(file_name=files)

class DIException(Exception):
    def __init__(self, status, code, msg):
        self.status = status
        self.code = code
        self.msg = msg
        Exception.__init__(self, self.status, "HTTP Status: %s, Code: %s, Message: %s" % (self.status, self.code, self.msg))

def _err_format(e):
    err = {}
    try:
        err = json.loads(e.body)
    except json.decoder.JSONDecodeError as je:
        err = {"code": "JSONDecodeError", "message": je}
    
    raise DIException(e.status, err["code"], err["message"]) from None