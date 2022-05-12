import requests
from threading import Thread


def download(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print("Sorry! Invalid URL")
        return

    # take last part of URL as filename
    slash_pos = url.rindex("/")    # look for / from the end
    filename = url[slash_pos + 1:]
    with open(filename, "wb") as f:
        f.write(resp.content)


while True:
    url = input("Enter URL [end to stop]: ")
    if url == "end":
        break

    t = Thread(target=download, args=(url,))
    t.start()

