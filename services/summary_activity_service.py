from sqlalchemy.orm import Session
from repositories.summary_activity_repository import SummaryActivityRepository
class SummaryActivityService:
    def __int__(self,session:Session):
        self.session = session
        self.summary_stats_repository = SummaryActivityRepository(self.session)
    def bulk_write(self,api_data):
        #write over all the data 
        #assume the api data is already structured like needed
        #from the APIClient
       self.summary_stats_repository.create(api_data)