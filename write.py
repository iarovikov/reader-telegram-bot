import os
from dotenv import load_dotenv, dotenv_values 
import datetime
import requests 
import json

load_dotenv()
token = os.getenv('READWISE_TOKEN')  # or however you're storing your token

response = requests.post(
        url="https://readwise.io/api/v3/save/",
        headers={"Authorization": f"Token {token}"}, verify=False,
        json={
            "url": "https://yourapp.com#document1",
            "html": "<p>Your document content here</p>",
        }
)

print(response.json())
