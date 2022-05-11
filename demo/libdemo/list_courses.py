from bs4 import BeautifulSoup

with open("courses.xml", "r") as f:
    contents = f.read()

bs = BeautifulSoup(contents, "xml")

for course in bs.find_all("course"):
    title = course.find('title').text
    duration = course.find('duration').text
    fee_tag = course.find('fee')
    currency = fee_tag['currency']  # Take value from currency attribute
    fee = fee_tag.text
    print(f"{title:20} - {duration:2} - {fee:4} {currency}")
