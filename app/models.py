from sqlalchemy import Column, Integer, Text, Float, DateTime
from datetime import datetime
from .database import Base

class ResumeMatch(Base):
    __tablename__ = "resume_matches"

    id = Column(Integer, primary_key=True, index=True)
    resume_text = Column(Text, nullable=False)
    job_description = Column(Text, nullable=False)
    score = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)