from typing import List,Optional
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import Integer,Float,BigInteger
from models.base import Base
class SummaryActivity(Base):
    __tablename__ = "summary_activity"
    id: Mapped[int] = mapped_column(BigInteger,primary_key=True)
    achievement_count:Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    average_speed :Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    average_watts:Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    elapsed_time:Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    elev_high:Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    elev_low:Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    max_speed:Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    moving_time:Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    total_elevation_gain:Mapped[Optional[float]] = mapped_column(Float, nullable=True)