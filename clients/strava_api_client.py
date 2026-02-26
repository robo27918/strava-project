from services.strava_token_service import StravaTokenService
class StravaAPIClient:
    def __init__(self):
        self.tokens_file = 'tokens.json'
        self.client = StravaTokenService(self.tokens_file).get_client()
    def fetch_summary_stats(self):
        return self.client.get_activities()
    
    