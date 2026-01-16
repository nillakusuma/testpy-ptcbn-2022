from fastapi import FastAPI
from app.routes import auth, master

app = FastAPI()

app.include_router(auth.router)
app.include_router(master.router)

@app.get("/")
def root():
    return {"message": "FastAPI jalan"}