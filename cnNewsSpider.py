#coding=utf-8

import urllib, urllib2 
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import string
import os
import re
import urllib
import hashlib
import time

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

from user_agents import user_agents
from config import URL_NEXT
from utils import extractMediaExpireDate, getRandomDomain, getRandomUserAgent

def extractNewsUrl(host):
	domain = getRandomDomain()
	# url = 'https://www.google.com.hk/search?q=' + searchWord.strip() + '&source=lnms&tbm=nws&num=20&as_qdr=n10'
	# url = URL_NEXT
	# url = url.format(domain = domain, query = searchWord.strip(), num = 5, qdr = 'n10')
	# url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=外交部%20陆慷&rn=50'
	url = host
	user_agent = getRandomUserAgent()
	headers = {
		'User-Agent': user_agent,
		'cookie': 'NID=126=rHiwWGEfr2VVtMOVvfLbZUa1FnGmWEo01MZlNN9DGJjGzdLfF342sf9gwVk8sGqQJUVWB8pp7d2Cpih9DUinHM17ITBtnmxGFVpC0Zz-8D0jCWnjIUSgLYCrBUP1bQVg9pHLyFQ; DV=c1EnZfFkERoSYKEIkm8vVLY3NacHJxY; 1P_JAR=2018-3-29-6'
		}

	req = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(req)

	soup = BeautifulSoup(response.read())

	# urls = [(item['href']) for item in soup.select('div#content_left div div.result h3 > a')]
	# print(urls)


	titleAndUrl = [(str(re.sub(u'<[\d\D]*?>', ' ', str(item))), item['href']) for item in soup.select('div#ires div.g h3 > a')]
	# titleAndUrl = [(title.strip(), rawUrl.split('url=')[1]) for title, rawUrl in titleAndRawUrl]
	rawSourceAndTime = [re.sub(u'<[\d\D]*?>', ' ', str(item)) for item in soup.select('div#ires div.g div.slp')]

	zippedData = list(zip(titleAndUrl, rawSourceAndTime))
	# print(zippedData)
	# titleAndUrl = [(re.sub(u'<[\d\D]*?>', ' ', str(item)), item['href']) for item in soup.select('div#ires div.g h3 > a')]

	
	print("=========")
	return zippedData

if __name__ == '__main__':
	cnTargetNewsPlatformUrl = 'https://www.google.com.hk/search?q=外交部+陆慷&newwindow=1&safe=strict&source=lnms&tbm=nws&sa=X&ved=0ahUKEwiD-bGg7_rdAhWKwMQHHbCWD9kQ_AUIDigB&biw=1280&bih=698&dpr=2&num=3&tbs=qdr:d,sbd:1'
	extractNewsUrl(cnTargetNewsPlatformUrl)
