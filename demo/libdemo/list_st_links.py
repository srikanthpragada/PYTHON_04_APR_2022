import requests
from bs4 import BeautifulSoup

#WEBSITE = "http://www.srikanthtechnologies.com"
WEBSITE = "https://www.w3schools.com"

resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, 'html.parser')

links = bs.find_all("a")
for link in links:
    href = link['href']
    if href == '#':
        continue

    if not href.startswith("http"):   # relative URL
        if href[0] != '/':
            href = WEBSITE + "/" + href
        else:
            href = WEBSITE + href

    print(href)
