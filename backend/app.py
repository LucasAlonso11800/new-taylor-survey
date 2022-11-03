from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def works():
    return "Yes"