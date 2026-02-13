import os
import json
from stravalib import Client
from dotenv import load_dotenv
import time
load_dotenv()
class StravaClientTokenService:
    '''
        ClientTokenService
            - creates a client with token authorization
            - loads token from file
            -saves new token after old token has expired
            -creates client to be used with always valid token
        
    '''
    def __init__(self, tokens_file):
        self.tokens_file=tokens_file
     
        self.client_id = os.getenv("STRAVA_CLIENT_ID")
        self.client_secret = os.getenv("STRAVA_CLIENT_SECRET")
        self.refresh_token = os.getenv("REFRESH_TOKEN")
        self.tokens = self.load_tokens()
        self.access_token = self.tokens['access_token']
        

    def load_tokens(self):
        """
            load tokens from file 
            or return an empty dict if file missing
        """
        if os.path.exists(self.tokens_file):
            with open(self.tokens_file,"r") as f:
                print("load successful")
                return json.load(f)
        else:
            print("FAILED TO LOAD FILE")
            return {}
    
    def save_token(self,tokens):
        with open(self.tokens_file,"w") as f:
            json.dump(tokens,f,indent=2)
        print("=="*10,"TOKEN SAVED", "=="*10)
    def get_client(self):
        client = Client()
        client.access_token = self.access_token
        client.refresh_token = self.refresh_token
        client.client_id = self.client_id
        client.client_secret = self.client_secret
        if self.tokens['expires_at']<time.time():
            print("Access token expired, updating token...")
            refresh_response = client.refresh_access_token(
                self.client_id,
                self.client_secret,
                self.refresh_token
            )
            self.tokens.update(refresh_response)
            self.save_token(self.tokens)
            client.access_token = refresh_response['access_token']
        return client