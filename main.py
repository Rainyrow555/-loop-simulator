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

