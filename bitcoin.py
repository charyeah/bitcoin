#https://price.btcfans.com/
import requests
import os
from lxml import etree
#MAX，MIN设置在secrets中
max=10000;min=4000;sendemail=False
url='https://price.btcfans.com/'
html = etree.HTML(requests.get(url).text)
price = float(html.xpath('//li[@id="coin-bitcoin"]//span[@class="last-price"]/text()')[0].replace(',',''))
info="现在的比特币价格是 1BTC = ${0}. ".format(price)
if (price>max):
    sendemail=True
    info+="It is recommended to sell."
if (price<min):
    sendemail=True
    info+="It is recommended to buy."
#生成html
print("::set-env name=sendemail::{}".format(sendemail))