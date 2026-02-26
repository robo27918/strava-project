from sqlalchemy.orm import Session
from services.summary_activity_service import SummaryActivityService
from clients.strava_api_client import StravaAPIClient
class IngestionService:
    def __init__(self,session:Session):
        self.session = session
        self.strava_api_client = StravaAPIClient()

    def ingest_summary_stats_only(self)->dict:
        self._ingest_summary_stats()
        print("ingested summary stats!")
    
    def _ingest_summary_stats(self):
        try:
            api_data = self.strava_api_client.fetch_summary_stats()
            #TODO: need to transform BatchedResultsIterator (api_data)
            # print("api_data: ",list(api_data))
            # print("api_data type: ",type(api_data))
            activities = [
                activity.__dict__
                for activity in api_data
            ]
            print(activities)
            sum_stat_service = SummaryActivityService(self.session)
            sum_stat_service.bulk_write(activities)
            return api_data
        except Exception as e:
            print("Summary Stats Ingestion Failed!", e)
            return {"succeeded":0 , "failed":1, "error":str(e)}
    