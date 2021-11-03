from . import _create_sw_client, _err_format
import swagger_client as sw
from swagger_client.models.insight import Insight
from swagger_client.models.patch_action import PatchAction
import json

class Insights():
    def __init__(self, team_id, project_id, host, token=None) -> None:
        self.team_id = team_id
        self.project_id = project_id
        self.sw_client = _create_sw_client(host, token)
        self.api = sw.InsightsApi(self.sw_client)
        self.token = token

    def create(self, id, subject, summary, content):
        body = Insight(id=id, subject=subject, summary=summary, content=content)
        try:
            self.api.update_insight(team_id=self.team_id, project_id=self.project_id, insight_id=id, body=body)
        except sw.rest.ApiException as e:
            _err_format(e)

    def update(self, id, prop, value):
        body = PatchAction("UPDATE", prop, value)

        try:
            self.api.update_insight_property(team_id=self.team_id, project_id=self.project_id, insight_id=id, body=body)
        except sw.rest.ApiException as e:
            _err_format(e)