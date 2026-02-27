from sqlalchemy.orm import Session
from .models import ResumeMatch

def save_match(db: Session, resume: str, job_desc: str, score: float):
    db_entry = ResumeMatch(
        resume_text=resume,
        job_description=job_desc,
        score=score
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry