#!/usr/bin/python
#-*-coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import codecs




DOWNLOAD_URL = 'http://www.kan2008.com/forum-66-1.html'


def download_html(url):
    print url
    return requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}).content

def parse_html(html):
    
    soup = BeautifulSoup(html, "lxml")
    root = soup.find('div', attrs={'class': 'boardnav'})
    for list in  root.find_all('tbody', attrs={'id': re.compile(r'normalthread_\d+')}):
        #print list
        info = list.find('th')
        #print info
        link = 'http://www.kan2008.com/' + info.a['href']
        title = info.a.string
        print link
        print title
    next = soup.find('span', attrs={'id': 'fd_page_bottom'}).find('a', attrs={'href': re.compile(r'forum-\d+-\d+.html')}, text="下一页")
    nextPage = 'http://www.kan2008.com/'+next['href']
    if next:
        return nextPage
    else:
        return None    

def main():
    url = DOWNLOAD_URL
    while url:
        html = download_html(url)
        url = parse_html(html)


if __name__ == '__main__':
    main()
