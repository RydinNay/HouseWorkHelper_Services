import os
from dotenv import load_dotenv

import requests
import json

load_dotenv()

_url = str(os.getenv('requests_main_url'))


def start_request(telephone):
    headers = ""
    response = requests.get(_url+'tg_bot_main/start', params={'phone': telephone}, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data
    return None
