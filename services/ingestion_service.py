from sqlalchemy.orm import Session
from services.summary_statistics_service import SummaryStatisticService

class IngestionService:
    def __init__(self,session:Session):
        self.session = session
        self.strava_api_client = StravaAPIClient()

    def ingest_summary_stats_only(self)->dict:
        self._ingest_summary_stats()
        print("ingested summary stats!")
    
    def _ingest_summary_stats():
        try:
            api_data = self.strava_api_client.fetch_summary_stats()
            sum_stat_service = SummaryStatisticService(self.session)
            sum_stat_service.bulk_write(api_data)
            return api_data
        except Exception as e:
            print("Summary Stats Ingestion Failed!", e)
            return {"succeeded":0 , "failed":1, "error":str(e)}
    