from dbconfig import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class QuestionSet(Base):
    __tablename__ = "questions_set"

    question_set_id = Column(Integer, primary_key=True, index=True)
    question_set_title = Column(String, unique=True, index=True)
    question_set_order = Column(Integer, unique=True, index=True)

    questions = relationship("Question")
    options = relationship("Option")

class Question(Base):
    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String)
    question_question_set_id = Column(Integer, ForeignKey("questions_set.question_set_id"))
    
class Option(Base):
    __tablename__ = "options"

    option_id = Column(Integer, primary_key=True, index=True)
    option_text = Column(String)
    option_question_set_id = Column(Integer, ForeignKey("questions_set.question_set_id"))
    
class Answer(Base):
    __tablename__ = "answers"
    
    answer_id = Column(Integer, primary_key=True, index=True)
    answer_option_id = Column(Integer, ForeignKey("options.option_id"))
    answer_question_id = Column(Integer, ForeignKey("questions.question_id"))