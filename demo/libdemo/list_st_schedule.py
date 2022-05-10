import requests
from bs4 import BeautifulSoup

WEBSITE = "http://www.srikanthtechnologies.com"

resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, 'html.parser')

schedule_table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
for row in schedule_table.find_all("tr")[1:]:
    cols = row.find_all("td")
    name = cols[0].text
    timings = cols[1].text
    stdate = cols[2].text
    print(f"{name:30} {timings:15} {stdate:10}")
