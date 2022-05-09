import requests

resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)

countries = resp.json()  # Convert JSON to dict

for c in sorted(countries, key=lambda cnt: cnt['population'], reverse=True)[:10]:
    capital = c.get('capital', ['None'])[0]
    print(f"{c['name']['common']:50} {capital:20} {c['area']:10}  {c['population']:10}")
