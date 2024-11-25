# 🚀 Roblox Trading Helper API

The **Roblox Trading Helper API** provides data for Roblox traders, including RAP (Recent Average Price), inventory values, item details, trade ads, and activity data using [Rolimon's API](https://www.rolimons.com/).

---

## 🌟 Features

- Fetch player RAP and inventory value.
- Retrieve item details like trends and market values.
- Access recent trade ads for trading insights.
- View platform-wide activity stats.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/roblox-trading-helper-api.git
cd roblox-trading-helper-api
```

2. Install Dependencies
Make sure you have Python 3.8 or later installed.
```bash
pip install -r requirements.txt
```

3. Run the API Locally
Start the FastAPI server using uvicorn:
```bash
uvicorn main:app --reload
```
The API will be available at http://127.0.0.1:8000.

# 📖 API Endpoints
## Root Endpoint

    GET /
    Returns a welcome message with usage instructions.

## Player Data

    GET /player/{user_id}
    Fetches data like RAP and inventory value for a Roblox player.

## Item Details

    GET /items
    Retrieves details for all trading items, including trends.

## Trade Ads

    GET /trade_ads
    Fetches recent trade advertisements.

## Activity Data

    GET /activity
    Displays platform-wide trading activity stats.
