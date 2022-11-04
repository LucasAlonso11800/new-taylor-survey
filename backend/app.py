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
@app.get('/question-set/{order}')
def get_question_set(order: int, db: Session = Depends(get_db)):
    questionSet = db.query(models.QuestionSet).where(models.QuestionSet.question_set_order == order).first()
    if questionSet is None:
        return { "error": True, "message": "Question set not found" }

    questions = db.query(models.Question.question_id, models.Question.question_text)\
                    .where(models.Question.question_id == models.QuestionSet.question_set_id)\
                    .all()
    options = db.query(models.Option.option_id, models.Option.option_text)\
                .where(models.Option.option_question_set_id == models.QuestionSet.question_set_id)\
                .all()

    return { "error": False, 
            "message": "", 
            "data": { "questionSet": questionSet, "questions": questions, "options": options }
            }

# Insert answer
@app.post('/answer')
def insert_answer(answer: schemas.Answer, db: Session = Depends(get_db)):
    question = db.query(models.Question).where(models.Question.question_id == answer.answer_question_id).first()
    option = db.query(models.Option).where(models.Option.option_id == answer.answer_option_id).first()

    if question is None:
        return { "error": True, "message": "Question not found" }
    elif option is None:
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