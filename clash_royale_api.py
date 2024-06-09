import os
import json
from dotenv import load_dotenv
from jwt_utils import get_request
import urllib.request
from datetime import datetime, timedelta, timezone
import sys

# Set the default encoding to utf-8
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables
load_dotenv()

# Environment variables
baseUrl = "https://api.clashroyale.com/v1"
clan_tag = os.getenv('CLAN_TAG')
player_id = os.getenv('PLAYER_ID')

# Debugging: Print environment variables to verify
print(f"CLAN_TAG: {clan_tag}")
print(f"CLAN_SECRET: {os.getenv('CLAN_SECRET')}")
print(f"PLAYER_ID: {player_id}")

# Function to retrieve clan information
def get_clan_info():
    endpoint = f"/clans/%23{clan_tag}"
    request = get_request(endpoint, baseUrl)
    
    # Debugging: Print the request URL and headers
    print(f"Request URL: {request.full_url}")
    print(f"Request Headers: {request.headers}")

    response = urllib.request.urlopen(request).read().decode("utf-8")
    data = json.loads(response)
    return data

# Function to retrieve and print player battle log
def get_player_battlelog(player_id):
    endpoint = f"/players/%23{player_id}/battlelog"
    request = get_request(endpoint, baseUrl)
    
    # Debugging: Print the request URL and headers
    print(f"Request URL: {request.full_url}")
    print(f"Request Headers: {request.headers}")

    response = urllib.request.urlopen(request).read().decode("utf-8")
    data = json.loads(response)
    
    # Print the battle log data
    print("Player Battle Log")
    print("=================")
    print(json.dumps(data, indent=4))

    # Summarize and print each battle
    summaries = summarize_battles(data)
    for summary in summaries:
        print(summary)

# Function to summarize battles
def summarize_battles(battles):
    summaries = []
    for battle in battles:
        try:
            battle_type = battle.get('type', 'Unknown')
            battle_time = battle.get('battleTime', 'Unknown')
            arena_name = battle.get('arena', {}).get('name', 'Unknown Arena')
            team = battle.get('team', [{}])[0]
            opponent = battle.get('opponent', [{}])[0]
            team_name = team.get('name', 'Unknown')
            team_crowns = team.get('crowns', 0)
            opponent_name = opponent.get('name', 'Unknown')
            opponent_crowns = opponent.get('crowns', 0)
            summary = (f"Type: {battle_type}, Time: {battle_time}, Arena: {arena_name}, "
                       f"Team: {team_name} ({team_crowns} crowns) vs "
                       f"Opponent: {opponent_name} ({opponent_crowns} crowns)")
            summaries.append(summary)
        except Exception as e:
            print(f"Error summarizing battle: {e}")
    return summaries

# Function to log player data
def log_player_data(clan_data, log_file='clan_log.json'):
    try:
        with open(log_file, 'r') as file:
            log_data = json.load(file)
    except FileNotFoundError:
        log_data = {}

    current_time = datetime.now(timezone.utc).isoformat()
    for member in clan_data['memberList']:
        player_tag = member['tag']
        if player_tag not in log_data:
            log_data[player_tag] = {
                'name': member['name'],
                'join_date': current_time,
                'last_seen': member['lastSeen'],
                'role': member['role'],
                'trophies': member['trophies']
            }
        else:
            log_data[player_tag]['last_seen'] = member['lastSeen']
            log_data[player_tag]['role'] = member['role']
            log_data[player_tag]['trophies'] = member['trophies']

    with open(log_file, 'w') as file:
        json.dump(log_data, file, indent=4)

# Function to display join dates
def display_join_dates(log_file='clan_log.json'):
    try:
        with open(log_file, 'r') as file:
            log_data = json.load(file)
    except FileNotFoundError:
        print("No log file found.")
        return

    print("Player Join Dates")
    print("=================")
    for player_tag, player_data in log_data.items():
        print(f"Name: {player_data['name']}, Tag: {player_tag}, Join Date: {player_data['join_date']}, Last Seen: {player_data['last_seen']}, Trophies: {player_data['trophies']}")

def display_clan_info(clan_data):
    print("Clan Information")
    print("================")
    print(f"Name: {clan_data['name']}")
    print(f"Tag: {clan_data['tag']}")
    print(f"Type: {clan_data['type']}")
    print(f"Description: {clan_data['description']}")
    print(f"Location: {clan_data['location']['name']}")
    print(f"Clan Score: {clan_data['clanScore']}")
    print(f"Clan War Trophies: {clan_data['clanWarTrophies']}")
    print(f"Required Trophies: {clan_data['requiredTrophies']}")
    print(f"Donations Per Week: {clan_data['donationsPerWeek']}")
    print(f"Members: {clan_data['members']}/50")
    print()

def display_active_members(clan_data, days=7):
    print("Active Members")
    print("==============")
    
    # Calculate the cutoff date
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)
    
    # Filter active members
    active_members = [
        member for member in clan_data['memberList']
        if datetime.strptime(member['lastSeen'][:-5], "%Y%m%dT%H%M%S").replace(tzinfo=timezone.utc) > cutoff_date
    ]

    # Display active members
    for member in active_members:
        print(f"Name: {member['name']}, Tag: {member['tag']}, Last Seen: {member['lastSeen']}, Trophies: {member['trophies']}")
    print()

def display_top_donors(clan_data, top_n=10):
    print(f"Top {top_n} Donors")
    print("================")

    sorted_members = sorted(clan_data['memberList'], key=lambda x: x['donations'], reverse=True)
    top_donors = sorted_members[:top_n]

    for member in top_donors:
        print(f"Name: {member['name']}, Tag: {member['tag']}, Donations: {member['donations']}")
    print()

def display_members_by_trophies(clan_data):
    print("Members Sorted by Trophies")
    print("==========================")

    sorted_members = sorted(clan_data['memberList'], key=lambda x: x['trophies'], reverse=True)

    for member in sorted_members:
        print(f"Name: {member['name']}, Tag: {member['tag']}, Trophies: {member['trophies']}, Role: {member['role']}")
    print()

def main():
    # Retrieve clan data from the API
    clan_data = get_clan_info()
    
    # Log player data
    log_player_data(clan_data)

    # Display general clan information
    display_clan_info(clan_data)

    # Display active members (seen within the last 7 days)
    display_active_members(clan_data, days=7)

    # Display top 10 donors
    display_top_donors(clan_data, top_n=10)

    # Display members sorted by trophies
    display_members_by_trophies(clan_data)

    # Display join dates
    display_join_dates()

    # Retrieve and print the battle log for the specified player
    get_player_battlelog(player_id)

# Entry point of the script
if __name__ == "__main__":    
    try:
        main()
    except urllib.error.HTTPError as e:
        print(f"HTTP error occurred: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error occurred: {e.reason}")