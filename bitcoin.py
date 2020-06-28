#https://price.btcfans.com/
import requests
from lxml import etree
import os
max=10000
min=4000
sendemail=False
url='https://price.btcfans.com/'
html = etree.HTML(requests.get(url).text)
price = html.xpath('//li[@id="coin-bitcoin"]//span[@class="last-price"]/text()')[0].replace(',','')
if (price>max):
    sendemail=True
    info="Sell out"
if (price<min):
    sendemail=True
    info="Bug in"
