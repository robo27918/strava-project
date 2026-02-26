from typing import List,Optional
from sqlalchemy.orm import Session
from models.summary_activity import SummaryActivity
from repositories.base_repository import BaseRepository

class SummaryActivityRepository(BaseRepository):
    def __init__(self,session:Session):
        super().__init__(SummaryActivity,session)