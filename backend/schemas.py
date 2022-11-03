from pydantic import BaseModel

class QuestionSet(BaseModel):
    question_set_id: int
    question_set_title: str 
    question_set_order: int

class Question(BaseModel):
    question_id: int
    question_text: str
    question_set_id: int

class Option(BaseModel):
    option_id: int
    option_text: str
    question_id: int

class Answer(BaseModel):
    answer_id: int
    option_id: int