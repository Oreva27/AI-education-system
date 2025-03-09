from fastapi import FastAPI

app = FastAPI()  # This is the ASGI app instance

@app.get("/")  
def home():  
    return {"message": "AI Education System API is running!"}
