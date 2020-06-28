#https://price.btcfans.com/
import requests
import os
from lxml import etree
max=10000;min=4000;sendemail=False;info=''
url='https://price.btcfans.com/'
html = etree.HTML(requests.get(url).text)
price = float(html.xpath('//li[@id="coin-bitcoin"]//span[@class="last-price"]/text()')[0].replace(',',''))
if (price>max):
    sendemail=True
    info="The current bitcoin price is ${0}, it is recommended to sell".format(price)
if (price<min):
    sendemail=True
    info="The current bitcoin price is ${0}, it is recommended to buy".format(price)
print("::set-env name=sendemail::{}".format(sendemail))
print("::set-env name=info::{}".format(info))
