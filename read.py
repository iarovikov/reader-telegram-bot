import os
from dotenv import load_dotenv, dotenv_values 
import datetime
import requests 
import json

load_dotenv()
token = os.getenv('READWISE_TOKEN')  # or however you're storing your token

def fetch_reader_document_list_api(updated_after=None, location=None):
    full_data = []
    next_page_cursor = None
    while True:
        params = {}
        if next_page_cursor:
            params['pageCursor'] = next_page_cursor
        if updated_after:
            params['updatedAfter'] = updated_after
        if location:
            params['location'] = location
        print("Making export api request with params " + str(params) + "...")
        response = requests.get(
            url="https://readwise.io/api/v3/list/",
            params=params,
            headers={"Authorization": f"Token {token}"}, verify=False
        )
        full_data.extend(response.json()['results'])
        next_page_cursor = response.json().get('nextPageCursor')
        if not next_page_cursor:
            break
    return full_data

# Get all of a user's documents from all time
# all_data = fetch_reader_document_list_api()

# Get all of a user's archived documents
# archived_data = fetch_reader_document_list_api(location='archive')

# Later, if you want to get new documents updated after some date, do this:
docs_after_date = datetime.datetime.now() - datetime.timedelta(days=3)  # use your own stored date
new_data = fetch_reader_document_list_api(docs_after_date.isoformat())

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)
