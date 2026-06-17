import requests
from requests.auth import HTTPBasicAuth
import json

USERNAME = "mixpanel_service_account"
PASSWORD = "mixpanel_secret"

r = requests.get(
    "https://mixpanel.com/api/query/segmentation",
    params={
        "event": '["$any_event"]',
        "type": "unique",
        "unit": "day",
        "from_date": "2026-06-10",
        "to_date": "2026-06-17"
    },
    auth=HTTPBasicAuth(USERNAME, PASSWORD)
)

data = r.json()

with open("active_users.json", "w") as f:
    json.dump(data, f)
