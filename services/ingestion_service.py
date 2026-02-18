from sqlalchemy.orm import Session
from services.summary_statistics_service import SummaryStatisticService

class IngestionService:
    def __init__(self,session:Session):
        self.session = session
        self.stats = SummaryStatisticsClient()