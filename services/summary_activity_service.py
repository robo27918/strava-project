from sqlalchemy.orm import Session
from repositories.summary_activity_repository import SummaryActivityRepository
class SummaryActivityService:
    def __int__(self,session:Session):
        self.session = session
        self.summary_stats_repository = SummaryActivityRepository(self.session)
    
    def bulk_write(self,api_data):
        transformed_data = self._transform_api_data(api_data)
        self.summary_stats_repository.create(transformed_data)
    
    def _transform_api_data(self,api_data):
        return{
            "id":api_data['id'],
            "achievement_count":api_data['achievement_count'],
            "average_speed":api_data['average_speed'],
            "average_watts":api_data['average_watts'],
            "elev_high":api_data['elev_high'],       
            "elev_low":api_data['elev_low'],       
            "max_speed":api_data['max_speed'],
            "moving_time":api_data['moving_time'],       
            "total_elevation_gain":api_data['total_elevation_gain'],       
        }