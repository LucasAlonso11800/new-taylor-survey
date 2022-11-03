from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

@app.get('/')
def works():
    return "Yes"

# Get question set with questions and their options
# Insert answer
# Get answer count for options in a question in a question set