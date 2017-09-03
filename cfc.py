#!/usr/bin/python
#-*-coding:utf-8 -*-

import codecs
import re
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://bbs.comefromchina.com/forums/5/'
index = 2


def download_page(url):
    print url
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content

def parse_post(html):
    soup = BeautifulSoup(html, "lxml")
    title = soup.find('body', attrs={'class': 'node5'}).find('div', attrs={'class': 'titleBar'})
    print "Post_Title ------->[%s]"%title.h1.string
    root = soup.find('ol', attrs={'class':'messageList', 'id':'messageList'})
    i = 0
    for list in root.find_all('li', attrs={'id': re.compile(r'post-\d+'), 'class':'message'}):
        i += 1
        print "Post%d Author:%s"%(i, list['data-author'])
        message = list.find('div', attrs={'class':'messageContent'})
        print message.get_text('|', strip=True)
        print "\n\n\n"
    try:
        next = soup.find('div', attrs={'id':'headerMover'}).find('div',attrs={'class':'PageNav'}).find('a',attrs={'href':re.compile(r'threads/\d+/page-\d+'),'class':'text'}, text="下一页 >")
    except AttributeError:
        pass
        next = None
    if next:
        return 'http://bbs.comefromchina.com/'+next['href']
    else:
        return None
def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    root = soup.find('div', attrs={'class':'discussionList'})
    leaf = root.find('ol', attrs={'class':'discussionListItems'})
    for list in leaf.find_all('li', attrs={'id':re.compile(r'thread-\d+')}):
        _, _, id = list['id'].partition('-')
        url = "http://bbs.comefromchina.com/threads/"+id
        print "post-------->"+url
        while url:
            html = download_page(url)
            url = parse_post(html)    
    next = soup.find('div', attrs={'class':'pageNavLinkGroup'}).find('div',attrs={'class':'PageNav'}).find('a',attrs={'href':re.compile(r'forums/\d+/page-\d+'),'class':'text'}, text="下一页 >")
    return "http://bbs.comefromchina.com/"+next['href']

def main():
    url = DOWNLOAD_URL
    while url:
        html = download_page(url)
        url = parse_html(html)

if __name__ == '__main__':
    main()

