from sqlalchemy.orm import Session
from repositories.summary_activity_repository import SummaryActivityRepository
class SummaryActivityService:
    def __init__(self,session:Session):
        self.session = session
        self.summary_stats_repository = SummaryActivityRepository(self.session)
    
    def write_to_db(self,api_data):
        try:
            transformed_data = self._transform_api_data(api_data)
            print("Getting ready to write to db via create method...")
            print("transformed_data",transformed_data)
            self.summary_stats_repository.create(**transformed_data)
            print("Successfully transformed data")
        except Exception as e:
            print("Error writing to DB",e)
    
    def _transform_api_data(self,api_data):
        try:
            return{
                "id":api_data['id'],
                "achievement_count":api_data.get('achievement_count',0),
                "average_speed":api_data.get('average_speed',0.0),
                "average_watts":api_data.get('average_watts',0.0),
                "elev_high":api_data.get('elev_high',0.0),
                "elapsed_time":api_data.get("elapsed_time",0),       
                "elev_low":api_data.get('elev_low',0.0),       
                "max_speed":api_data.get('max_speed',0.0),
                "moving_time":api_data.get('moving_time',0),       
                "total_elevation_gain":api_data.get('total_elevation_gain',0.0),       
            }
        except Exception as e:
            print("api_data",api_data)
            print("Data transfomration failed", e)
