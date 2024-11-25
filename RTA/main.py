from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

# Initialize the FastAPI app
app = FastAPI(
    title="Roblox Trading Helper API",
    description="🚀 A modern API to fetch Roblox trading data including RAP, inventory values, trends, and more from Rolimon's and Roblox APIs.",
    version="1.0.0",
)

# Add CORS middleware for frontend compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define helper functions for Rolimon's API integrations
ROLIMONS_BASE_URL = "https://www.rolimons.com"

def fetch_player_data(user_id: str):
    """
    Fetch player data from Rolimon's API.
    """
    url = f"{ROLIMONS_BASE_URL}/playerapi/player/{user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        raise HTTPException(status_code=400, detail="Failed to fetch data from Rolimon's API.")

def fetch_item_details():
    """
    Fetch item details from Rolimon's API.
    """
    url = f"{ROLIMONS_BASE_URL}/itemapi/itemdetails"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        raise HTTPException(status_code=400, detail="Failed to fetch item details from Rolimon's API.")

def fetch_recent_trade_ads():
    """
    Fetch recent trade advertisements from Rolimon's API.
    """
    url = f"{ROLIMONS_BASE_URL}/tradeadsapi/getrecentads"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        raise HTTPException(status_code=400, detail="Failed to fetch recent trade ads from Rolimon's API.")

def fetch_activity_data():
    """
    Fetch platform activity data from Rolimon's API.
    """
    url = f"{ROLIMONS_BASE_URL}/api/activity"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        raise HTTPException(status_code=400, detail="Failed to fetch activity data from Rolimon's API.")


# API Endpoints
@app.get("/player/{user_id}", tags=["Player Data"])
async def get_player_data(user_id: str):
    """
    Fetch player data using Rolimon's API.
    """
    data = fetch_player_data(user_id)
    return {"success": True, "data": data}


@app.get("/items", tags=["Item Details"])
async def get_item_details():
    """
    Fetch item details from Rolimon's API.
    """
    data = fetch_item_details()
    return {"success": True, "data": data}


@app.get("/trade_ads", tags=["Trade Ads"])
async def get_trade_ads():
    """
    Fetch recent trade ads from Rolimon's API.
    """
    data = fetch_recent_trade_ads()
    return {"success": True, "data": data}


@app.get("/activity", tags=["Activity"])
async def get_activity():
    """
    Fetch platform activity data from Rolimon's API.
    """
    data = fetch_activity_data()
    return {"success": True, "data": data}


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint with instructions.
    """
    return {
        "message": "Welcome to the Roblox Trading Helper API! Use /player/{user_id}, /items, /trade_ads, or /activity to fetch data."
    }

