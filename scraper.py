import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.co.uk/16-Inch-2-4ghz-8-Core-Deecies-Limited/dp/B0821LJM6M/ref=sr_1_9?dchild=1&keywords=macbook&qid=1591501857&sr=8-9'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}


def price_check():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    # Using a second soup allows me to add an extra level of indirection and bypasses the fact that Amazon makes its HTML code with JavaScript
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    price = soup2.find(id='priceblock_ourprice').get_text()

    int_price = float(price[1:].replace(',',''))

