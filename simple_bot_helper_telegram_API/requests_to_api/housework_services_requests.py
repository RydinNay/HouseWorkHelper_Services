import os
from dotenv import load_dotenv

import requests
import json

load_dotenv()

_url = os.getenv('requests_main_url')


def make_simple_housework_schedule(work_list):
    headers = ""
    response = requests.get(_url+"tg_bot/housework_simple_schedule", params={'work_list': work_list}, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data
    return None
