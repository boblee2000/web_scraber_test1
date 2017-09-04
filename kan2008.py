#!/usr/bin/python
#-*-coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import codecs
import os
import urllib
import urllib2


DOWNLOAD_URL = 'http://www.kan2008.com/forum-66-74.html'


def download_html(url):
    print url
    return requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}).content

def parse_post(html, path):
    soup = BeautifulSoup(html, "lxml")
    postToGetPic = soup.find('body', attrs={'id': 'nv_forum'}).find('div', attrs={'id':'ct', 'class':'wp'}).find('div', attrs={'id':re.compile('post_\d+')})
    for list in postToGetPic.find_all('ignore_js_op'):
        info = list.find('img', attrs={'id': re.compile(r'aimg_\d+')})
        title = info['title']
        print title
        page = list.find('a', attrs={'href': re.compile(r'^forum.php\?mod=attachment&aid=')})
        #print page
        link = 'http://www.kan2008.com/' + page['href']
        ##print link
        path2 = path + '/' + title
        #print path
        urllib.urlretrieve(link, path2)

    return None

def parse_html(html):
    
    soup = BeautifulSoup(html, "lxml")
    root = soup.find('div', attrs={'class': 'boardnav'})
    for list in  root.find_all('tbody', attrs={'id': re.compile(r'normalthread_\d+')}):
        info = list.find('th')
        link = 'http://www.kan2008.com/' + info.a['href']
        title = info.a.string
        path = 'pic/' + title
        #print link
        print title
        if not os.path.isdir(path):
            os.mkdir(path)
        html = download_html(link)
        parse_post(html, path)
    
    try:
        next = soup.find('span', attrs={'id': 'fd_page_bottom'}).find('a', attrs={'href': re.compile(r'forum-\d+-\d+.html')}, text="下一页")
        nextPage = 'http://www.kan2008.com/'+next['href']
    except TypeError:
        next = None

    if next:
        return nextPage
    else:
        return None    

def main():
    url = DOWNLOAD_URL
    if not os.path.isdir('pic'): os.mkdir('pic')
    while url:
        html = download_html(url)
        url = parse_html(html)


if __name__ == '__main__':
    main()
