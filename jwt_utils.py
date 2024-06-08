import jwt
import datetime
import os
from dotenv import load_dotenv
import urllib.request

# Load environment variables
load_dotenv()

# Environment variables
clan_secret = os.getenv('CLAN_SECRET')

def generate_jwt(issuer, subject, secret_key, expiration_days=1):
    payload = {
        'iss': issuer,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=expiration_days),
        'iat': datetime.datetime.now(datetime.timezone.utc),
        'sub': subject
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def get_request(endpoint, base_url):
    r = urllib.request.Request(
        base_url + endpoint, 
        None, 
        {"Authorization": f"Bearer {clan_secret}"}
    )
    return r