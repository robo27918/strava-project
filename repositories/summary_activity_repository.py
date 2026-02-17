from typing import List,Optional
from sqlalchemy.orm import Session
from models.summary_activity import SummaryActivity
from base_repository import BaseRepository

class SummaryActivity(BaseRepository):
    def __int__(self,session:Session):
        super().__int__(SummaryActivity,session)