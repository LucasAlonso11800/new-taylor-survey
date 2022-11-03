from fastapi import FastAPI
from dbconfig import conn
from models import questions_sets, questions, options, answers

app = FastAPI()

@app.get('/')
def works():
    return conn.execute(questions_sets.select()).fetchall()

# Get question set with questions and their options
# Insert answer
# Get answer count for options in a question in a question set