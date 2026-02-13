from dotenv import load_dotenv
from StravaClientTokenService import StravaClientTokenService
from pprint import pprint
load_dotenv()
service = StravaClientTokenService('tokens.json')
client = service.get_client()
activities = client.get_activities()

for a in activities:
   pprint(a.__str__())

