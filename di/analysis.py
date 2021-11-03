from . import _create_sw_client, _err_format, SSL
import swagger_client as sw
from swagger_client.models.analysis_job_status import AnalysisJobStatus

class Analytics():
    def __init__(self, host, token=None) -> None:
        self.sw_client = _create_sw_client(host, token)
        self.api = sw.AnalysisApi(self.sw_client)

    def adopt(self):
        try:
            return self.api.adopt_analaysis_job()
        except sw.rest.ApiException as e:
            if e.status != 404:
                _err_format(e)
    
    def report_status(self, team_id, job_id, status, message):
        try:
            jobStatus = AnalysisJobStatus(status=status, message=message)
            return self.api.report_analysis_status(team_id, job_id, body=jobStatus)
        except sw.rest.ApiException as e:
            _err_format(e)