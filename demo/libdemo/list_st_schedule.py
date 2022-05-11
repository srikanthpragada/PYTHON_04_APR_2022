import requests
from bs4 import BeautifulSoup
from datetime import *

WEBSITE = "http://www.srikanthtechnologies.com"

resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, 'html.parser')

schedule_table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
for row in schedule_table.find_all("tr")[1:]:
    cols = row.find_all("td")
    name = cols[0].text
    timings = cols[1].text
    stdate = cols[2].text
    cd = datetime.today()
    sd = datetime.strptime(f"{stdate}-{cd.year}", "%d-%b-%Y")
    #print(sd, cd)
    days = (sd.date() - cd.date()).days
    if days < 0:
        msg = "day(s) old"
    else:
        msg = "day(s) to go"
    print(f"{name:30} {timings:15} {stdate:10}  {abs(days)} {msg}")
