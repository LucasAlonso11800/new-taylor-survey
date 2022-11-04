from fastapi import FastAPI, Depends
from dbconfig import SessionLocal
import models, schemas
from sqlalchemy.orm import Session

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get question set with questions and their options

# Insert answer
@app.post('/answer')
def insert_answer(answer: schemas.Answer, db: Session = Depends(get_db)):
    question = db.query(models.Question).filter(models.Question.question_id == answer.answer_question_id).first()
    option = db.query(models.Option).filter(models.Option.option_id == answer.answer_option_id).first()

    if question == None:
        return { "error": True, "message": "Question not found" }
    elif option == None:
        return { "error": True, "message": "Option not found" }
    else:
        newAnswer = models.Answer(
            answer_question_id=answer.answer_question_id, 
            answer_option_id=answer.answer_option_id
        )
        db.add(newAnswer)
        db.commit()
        return { "error": False, "message": "" }

# Get answer count for options in a question in a question set