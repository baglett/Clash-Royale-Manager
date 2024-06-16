import os
import json
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone

# Load environment variables
load_dotenv()

# Environment variables
baseUrl = "https://api.clashroyale.com/v1"
clan_tag = os.getenv('CLAN_TAG')
player_id = os.getenv('PLAYER_ID')
bearer_token = os.getenv('LOCAL_CLAN_SECRET') if os.getenv('DB_ENVIRONMENT') == 'local' else os.getenv('CLAN_SECRET')

# Function to retrieve clan information
def get_clan_info():
    endpoint = f"/clans/%23{clan_tag}"
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(f"{baseUrl}{endpoint}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        response.raise_for_status()

# Function to retrieve player details
def get_player_details(player_tag):
    endpoint = f"/players/%23{player_tag}"
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(f"{baseUrl}{endpoint}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        response.raise_for_status()

# Function to retrieve player battle log
def get_player_battlelog(player_id):
    endpoint = f"/players/%23{player_id}/battlelog"
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(f"{baseUrl}{endpoint}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        response.raise_for_status()