import requests
import re

url = "/imgres?q=%E5%90%89%E4%BC%8A%E5%8D%A1%E5%93%87&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fzh%2Fthumb%2Fd%2Fd3%2F%25E5%2590%2589%25E4%25BC%258A%25E5%258D%25A1%25E5%2593%258701.jpg%2F250px-%25E5%2590%2589%25E4%25BC%258A%25E5%258D%25A1%25E5%2593%258701.jpg&imgrefurl=https%3A%2F%2Fzh.wikipedia.org%2Fzh-tw%2F%25E5%2590%2589%25E4%25BC%258A%25E5%258D%25A1%25E5%2593%2587&docid=hBeB6FPtgyHUMM&tbnid=gp8qFf2lNtFi_M&vet=12ahUKEwjV1ePoyZyPAxV2dPUHHSIXETwQM3oECBgQAA..i&w=250&h=355&hcb=2&ved=2ahUKEwjV1ePoyZyPAxV2dPUHHSIXETwQM3oECBgQAA"
pat=re.compile(r"imgurl=(.*(jpg|jpeg|png|gif))")
result = re.search(pat, url)
url = result.group(1)

from urllib.parse import urlparse, unquote
# url = "https%3A%2F%2Fhips.hearstapps.com%2Fhmg-prod%2Fimages%2F091308-66ebdf638a057.jpeg"
url = unquote(url)
print(url)
resp = requests.get(url, stream=True)
with open("test.jpg", "wb") as f:
    f.write(resp.raw.read())


