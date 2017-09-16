#!/usr/bin/python
#-*-coding:utf-8 -*-

import re
import requests
import random
from bs4 import BeautifulSoup


class gatherProxyCom(object):

	def __init__(self):
		self.proxy = []
		self.url = "http://www.gatherproxy.com/zh/"
		self.UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
		"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
       	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        )
		self.ua = self.UAS[random.randrange(len(self.UAS))]
		self.headers =  {'user-agent': self.ua}

	def getProxyIp(self):

		html = requests.get(self.url, headers=self.headers).content
		keyList = re.findall(r"\"PROXY_IP\"\:\"(?P<IP>.*?)\".*?\"PROXY_PORT\":\"(?P<PORT>.*?)\".*?\"PROXY_STATUS\":\"(?P<STATUS>.*?)\".*?\"PROXY_TIME\":\"(?P<DELAY>.*?)\"", html)
		for list in keyList:
			if list[2] == 'OK' and int(list[3]) < 500:
				self.proxy.append(list[0]+':'+str(int(list[1], 16)))
		return self.proxy

def main():
	kk = gatherProxyCom()
	kk.getProxyIp()

if __name__ == '__main__':
	main()