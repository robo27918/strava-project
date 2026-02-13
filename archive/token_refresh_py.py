import os
import json
from dotenv import load_dotenv
from stravalib import Client
from pprint import pprint

load_dotenv()

TOKENS_FILE = "tokens.json"

def load_tokens():
    """Load tokens from file, or return empty dict if file missing."""
    if os.path.exists(TOKENS_FILE):
        with open(TOKENS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_tokens(tokens):
    """Save access, refresh, and expiry info to file."""
    with open(TOKENS_FILE, "w") as f:
        json.dump(tokens, f, indent=2)
    print("✅ Tokens saved.")

def make_client():
    """Create a Strava client that refreshes tokens automatically."""
    tokens = load_tokens()
    client = Client(
        access_token=tokens.get("access_token"),
        refresh_token=tokens.get("refresh_token"),
        client_id=os.getenv("STRAVA_CLIENT_ID"),
        client_secret=os.getenv("STRAVA_CLIENT_SECRET"),
    )

    # If expired, refresh automatically
    if client.token_expires_at and client.token_expires_at < client.protocol.now():
        print("🔄 Access token expired — refreshing...")
        refresh_response = client.refresh_access_token(
            client_id=os.getenv("STRAVA_CLIENT_ID"),
            client_secret=os.getenv("STRAVA_CLIENT_SECRET"),
            refresh_token=tokens.get("refresh_token")
        )

        # Update and save tokens
        tokens.update(refresh_response)
        save_tokens(tokens)
        client.access_token = refresh_response["access_token"]

    return client


# === MAIN SCRIPT ===
if __name__ == "__main__":
    client = make_client()

    athlete = client.get_athlete()
    print(f"👋 Hello there, {athlete.firstname}!")
    pprint(athlete.to_dict())  # to_dict() works better than f-string with pprint

    print("\n🏃 Recent activities:")
    for activity in client.get_activities(limit=5):
        print(f"- {activity.name} ({activity.distance:.2f}m)")
