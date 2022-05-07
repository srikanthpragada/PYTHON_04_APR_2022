import requests

resp = requests.get("http://worldclockapi.com/api/json/utc/now")
d = resp.json()  # Convert JSON to dict
print(d['currentDateTime'])
