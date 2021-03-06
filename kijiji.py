#!/usr/bin/python
#-*-coding:utf-8 -*-

import codecs
import re
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://www.kijiji.ca/b-ottawa-gatineau-area/l1700184'
FILTER = 1
postNumber = 0
locationFilter = ['deepthroat']
catagoryFilter = ['v-cars-trucks']

def download_page(url):
    print url
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content

def parse_post(html):
    global postNumber,poster
    soup = BeautifulSoup(html, "lxml")
    title = soup.find('body', attrs={'class': 'node5'}).find('div', attrs={'class': 'titleBar'})
    print "Post_Title ------->[%s]"%title.h1.string
    root = soup.find('ol', attrs={'class':'messageList', 'id':'messageList'})
    i = 0
    QuoteText = None
    for list in root.find_all('li', attrs={'id': re.compile(r'post-\d+'), 'class':'message'}):
        if FILTER and list['data-author'] not in poster:
            continue
        postNumber += 1
        print "Post%d Author:%s"%(postNumber, list['data-author'])
        message = list.find('div', attrs={'class':'messageContent'})
        messageText = message.get_text(strip=True)
        for quote in list.find_all('div', attrs={'class':'bbCodeBlock'}):
            replacedText = quote.get_text(strip=True)
            messageText = messageText.replace(replacedText, '') 
            print "............................................"
            print "Quote from %s" % quote['data-author']
            QuoteText = quote.find('div', attrs={'class':'quote'})
            print QuoteText.get_text(strip=True)
        if QuoteText:        
            print "............................................"
        print messageText
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
    global postNumber,publisher

    soup = BeautifulSoup(html, "lxml")
    root = soup.find('div', attrs={'id':'MainContainer'})
    for list in root.find_all('div', attrs={'data-ad-id':re.compile(r'\d+')}):
        #print list
        title = list.find('div', attrs={'class':'title'})
        url = title.a['href']
        info = url.split('/')
        
        if FILTER and (info[1] not in catagoryFilter):
            continue
        location = list.find('div', attrs={'class':'location'}).get_text(strip=True)
        description = list.find('div', attrs={'class':'description'}).get_text(strip=True)
        price = list.find('div', attrs={'class':'price'}).get_text(strip=True)
        print 'url: '+url
        print 'location: '+location
        print 'decription: '+description
        print 'price: '+price
        print '\n\n\n\n'

    next = root.find('div', attrs={'class':'bottom-bar'}).find('div',attrs={'class':'pagination'}).find('a',attrs={'title':'Next'}, text='Next >')
    return "https://www.kijiji.ca"+next['href']

def main():
    url = DOWNLOAD_URL
    while url:
        html = download_page(url)
        url = parse_html(html)

if __name__ == '__main__':
    main()

