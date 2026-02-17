from typing import List,Optional
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import Integer,Float
from models.base import Base
class SummaryActivity(Base):
    __tablename__ = "summary_activity"
    id: Mapped[int] = mapped_column(primary_key=True)
    achievement_count:Mapped[int] = mapped_column(Integer)
    average_speed :Mapped[float] = mapped_column(Float)
    average_watts:Mapped[float] = mapped_column(Float)
    elapsed_time:Mapped[float] = mapped_column(Float)
    elev_high:Mapped[float] = mapped_column(Float)
    elev_low:Mapped[float] = mapped_column(Float)
    max_speed:Mapped[float] = mapped_column(Float)
    moving_time:Mapped[float] = mapped_column(Float)
    total_elevation_gain:Mapped[float] = mapped_column(Float)