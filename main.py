from fastapi import FastAPI
import os
import httpx

app = FastAPI()

NIGHTSCOUT_URL = os.getenv("NIGHTSCOUT_URL")

@app.get("/")
def read_root():
    return {"message": "Loop simulator backend running"}

@app.get("/bg")
async def get_bg_data():
    if not NIGHTSCOUT_URL:
        return {"error": "Nightscout URL not set"}

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{NIGHTSCOUT_URL}/api/v1/entries/sgv.json?count=10")
        data = response.json()
        return data
import httpx
from fastapi import FastAPI

app = FastAPI()

# Replace this with your actual Nightscout API URL (with /api/v1/)
NIGHTSCOUT_URL = "https://rainbow.oracle2.cgmsim.com/api/v1/entries/sgv.json?count=10"

@app.get("/bg")
async def get_bg():
    async with httpx.AsyncClient() as client:
        response = await client.get(NIGHTSCOUT_URL)
        data = response.json()
        if not data:
            return {"error": "No BG data found"}
        latest_bg = data[0]["sgv"]  # sgv = sensor glucose value
        timestamp = data[0]["dateString"]  # readable timestamp
        return {"latest_bg": latest_bg, "timestamp": timestamp}

