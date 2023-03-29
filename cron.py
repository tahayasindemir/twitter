from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
# from schemas import recommender
# burada base modellerimiz gösteriliyor
import joblib
import uvicorn

app = FastAPI()
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# sudo chown -R root:miuul /home/miuul/twitter
# sudo chmod 2775 /home/miuul/twitter && find /home/miuul/twitter -type d -exec sudo chmod 2775 {} \;

@app.get("/cron/username")
def get_twitter(fastapi_req: Request):
    return {"username": "ssss"}


if __name__ == "__main__":
    uvicorn.run("cron:app", host="0.0.0.0", port=8001, reload=True)
