import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.co.uk/adidas-Manchester-United-Jersey-Large/dp/B07R2B8GTF/ref=sr_1_5?dchild=1&keywords=manchester+united+top&qid=1591499606&sr=8-5'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

price = soup.find(id='priceblock_ourprice')

print(price)