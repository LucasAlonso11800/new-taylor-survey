from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from dbconfig import SessionLocal
import models, schemas
from sqlalchemy.orm import Session

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

    questions = db.query(models.Question.question_id, models.Question.question_text).all()

    options = db.query(models.Option.option_id, models.Option.option_text)\
                .where(models.Option.option_question_set_id == order)\
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
@app.get('/answer')
def get_answers(db: Session = Depends(get_db)):
    questionSet = db.query(models.QuestionSet).order_by(models.QuestionSet.question_set_order).all()
    questions = db.query(models.Question).all()
    options = db.query(models.Option).all()
    answers = db.query(models.Answer).all()

    response = {}

    for set in questionSet:
        setData = {}
        for question in questions:
            questionData = {}
            for option in options:
                if option.option_question_set_id != set.question_set_id:
                    continue

                questionData[option.option_text] = 0
                for answer in answers:
                    if answer.answer_option_id == option.option_id and\
                        answer.answer_question_id == question.question_id:
                        questionData[option.option_text] += 1

            setData[question.question_text] = questionData
        response[set.question_set_title] = setData
    
    return { "error": False, "message": "", "data": { "answers": response } }