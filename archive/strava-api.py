import json
import os
from dotenv import load_dotenv
from stravalib import Client
from pprint import pprint
load_dotenv()

client = Client()
response = client.exchange_code_for_token(
    client_id= os.getenv("STRAVA_CLIENT_ID"),
    client_secret= os.getenv("STRAVA_CLIENT_SECRET"),
    code =  os.getenv("CODE")
)
print("="*60)
pprint(response)
print("="*60)

client.access_token = os.getenv("ACCESS_TOKEN")
client.refresh_token = os.getenv("REFRESH_TOKEN")
client.client_secret= os.getenv("STRAVA_CLIENT_SECRET")
client.client_id = os.getenv("STRAVA_CLIENT_ID")

athlete=client.get_athlete()
print(f"Hello there {athlete.firstname}")
pprint(f"{athlete.dict()}")
pprint(athlete.stats.dict() )
activities = client.get_activities()
for a in activities:
    print(f"{a.average_speed}, {a.average_cadence} {a.average_watts} {a.moving_time}")



