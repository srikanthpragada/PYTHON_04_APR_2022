import requests

userid = input("Enter github user id :")
resp = requests.get(f"https://api.github.com/users/{userid}")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)

d = resp.json()  # Convert JSON to dict

print("Name        :", d['name'])
print("Company     :", d['company'])
print("Location    :", d['location'])
print("Public Repos:", d['public_repos'])

