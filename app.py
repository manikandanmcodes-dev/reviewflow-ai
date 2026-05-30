from fastapi import FastAPI
from webhook.receiver import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "ReviewFlow AI Running"
    }