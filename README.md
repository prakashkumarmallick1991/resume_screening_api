# resume_screening_api

# AI-Powered Resume Screening API

## Overview

AI-Powered Resume Screening API is a backend application that evaluates the similarity between a candidate's resume and a job description using Natural Language Processing and Machine Learning.

The system processes text input, computes a similarity score using TF-IDF vectorization and cosine similarity, classifies the candidate as Suitable or Not Suitable, and stores the results in a PostgreSQL database.

This project demonstrates backend architecture, NLP preprocessing, ML integration, and database persistence in a modular production-style structure.

---

## Tech Stack

Backend:

* FastAPI
* Uvicorn

Machine Learning:

* Scikit-learn (TF-IDF, cosine similarity)
* NumPy

NLP:

* spaCy

Database:

* PostgreSQL
* SQLAlchemy ORM
* psycopg2

Environment Management:

* python-dotenv
* Virtual environment

---

## Project Architecture

```
Client
   ↓
FastAPI
   ↓
NLP Preprocessing (spaCy)
   ↓
TF-IDF Vectorization
   ↓
Cosine Similarity
   ↓
PostgreSQL (SQLAlchemy)
```

---

## Features

* Resume and Job Description similarity scoring
* NLP text preprocessing (lemmatization, stopword removal)
* TF-IDF based feature extraction
* Cosine similarity scoring
* Candidate classification (Suitable / Not Suitable)
* PostgreSQL data persistence
* Modular backend architecture
* Auto-generated API documentation

---

## Input Format

POST `/match`

```json
{
  "resume": "Python developer with machine learning experience",
  "job_description": "Looking for ML engineer with Python skills"
}
```

---

## Output Format

```json
{
  "score": 0.78,
  "decision": "Suitable"
}
```

The result is also stored in the database with timestamp.

---

## Database Schema

Table: `resume_matches`

| Column          | Type                  |
| --------------- | --------------------- |
| id              | Integer (Primary Key) |
| resume_text     | Text                  |
| job_description | Text                  |
| score           | Float                 |
| created_at      | DateTime              |

---

## Project Structure

```
resume_screening_api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── nlp.py
│   ├── ml.py
│   └── crud.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/prakashkumarmallick1991/resume_screening_api.git
cd resume_screening_api
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Configure Environment

Create `.env` file:

```
DATABASE_URL=postgresql://username:password@localhost:5432/resume_db
```

### 5. Create Database

Using pgAdmin or psql:

```
CREATE DATABASE resume_db;
```

### 6. Run Application

```
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI available at:

```
http://127.0.0.1:8000/docs
```

---

## What This Project Demonstrates

* Modular backend system design
* REST API development
* NLP preprocessing pipeline
* Feature engineering with TF-IDF
* Similarity scoring using cosine similarity
* ORM-based database integration
* Environment-based configuration management

---

## Future Improvements (Not Yet Implemented)

* Authentication
* Model persistence
* Advanced embeddings (BERT)
* Resume PDF parsing
* Frontend interface
* Dockerized deployment

---

## Author

Prakash Kumar

Which direction do you want?

