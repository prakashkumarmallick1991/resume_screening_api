from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .schemas import ResumeRequest, ResumeResponse
from .nlp import preprocess
from .ml import compute_similarity
from .crud import save_match

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Resume Screening API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/match", response_model=ResumeResponse)
def match_resume(data: ResumeRequest, db: Session = Depends(get_db)):

    clean_resume = preprocess(data.resume)
    clean_jd = preprocess(data.job_description)

    score = compute_similarity(clean_resume, clean_jd)

    decision = "Suitable" if score > 0.65 else "Not Suitable"

    save_match(db, data.resume, data.job_description, score)

    return {
        "score": score,
        "decision": decision
    }