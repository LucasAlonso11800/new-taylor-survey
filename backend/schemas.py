from typing import Optional
from pydantic import BaseModel

class QuestionSet(BaseModel):
    question_set_id: int
    question_set_title: str 
    question_set_order: int

class Question(BaseModel):
    question_id: int
    question_text: str

class Option(BaseModel):
    option_id: int
    option_text: str
    option_question_set_id: int

class Answer(BaseModel):
    answer_id: Optional[int]
    answer_option_id: int
    answer_question_id: int