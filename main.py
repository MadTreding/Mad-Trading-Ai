from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    return {
        "signal": "LONG",
        "success_rate": 83,
        "entry": 1.2450,
        "stop_loss": 1.2380,
        "take_profit": 1.2620,
        "reasons": ["Bullish momentum", "RSI > 50", "Support bounce"]
    }
