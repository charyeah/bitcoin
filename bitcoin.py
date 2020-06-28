#https://price.btcfans.com/
import requests
import os
from lxml import etree
from jinja2 import Environment, PackageLoader
#MAX，MIN设置在secrets中
max=10000;min=4000
sendemail=False;strategy="继续持有"
url='https://price.btcfans.com/'
html = etree.HTML(requests.get(url).text)
price = float(html.xpath('//li[@id="coin-bitcoin"]//span[@class="last-price"]/text()')[0].replace(',',''))
if (price>max):
    sendemail=True
    strategy="卖出"
if (price<min):
    sendemail=True
    strategy="买入"
env = Environment(loader=PackageLoader('bitcoin', ''))
template = env.get_template('template.html')
template.stream(price=price,max=max,min=min,strategy=strategy).dump('email.html')
print("::set-env name=sendemail::{}".format(sendemail))