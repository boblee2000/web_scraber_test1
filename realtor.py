#!/usr/bin/python
#-*-coding:utf-8 -*-

import codecs
import re
import requests
from bs4 import BeautifulSoup
import http
import random

DOWNLOAD_URL = 'https://www.realtor.ca/'
FILTER = 1
postNumber = 0
publisher = ['deepthroat']
poster = ['deepthroat']

Cookie = {
    "__qca":"P0-790114168-1501392557222", "__utma":"151806763.485722766.1501392556.1503617627.1503623980.2", "__utmc":"151806763", "__utmz":"151806763.1503623980.2.2.utmcsr=bbs.comefromchina.com|utmccn=(referral)|utmcmd=referral|utmcct=/threads/880733/page-4", "xfa_user":"127809%2Ca2949cb8acf1b54363ceb0a9d3f78fb6f517f966", "xfa_session":"8e5844c7732e0e69922da55d811b0099", "_ga":"GA1.2.485722766.1501392556", "_gid":"GA1.2.1655723088.1504142767", "_gat":'1', "__asc":"0a6bbb3b15e4f66d58612d00be2", "__auc":"e76f6d0b15d91f852c2d2c6b194"
}

proxies = {"https": "185.5.18.164:3128", "https": "23.94.234.42:8080", "https": "45.76.6.86:3128", "https": "35.187.227.175:8080"}  

UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1", 
       "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
       )

ua = UAS[random.randrange(len(UAS))]
headers = {'user-agent': ua}



session = None

loginUrl = 'https://api2.realtor.ca/Listing.svc/PropertySearch_Post'
postData = {
    'CultureId':'1',
    'ApplicationId':'1',
    'RecordsPerPage':'9',
    'MaximumResults':'9',
    'PropertySearchTypeId':'3',
    'TransactionTypeId':'2',
    'StoreyRange':'0-0',
    'BedRange':'0-0',
    'BathRange':'0-0',
    'OwnershipTypeGroupId':'2',
    'LongitudeMin':'-81.86698576416018',
    'LongitudeMax':'-74.01176115478518',
    'LatitudeMin':'41.02707659739538',
    'LatitudeMax':'47.37373046918453',
    'SortOrder':'A',
    'SortBy':'1',
    'viewState':'m',
    'Longitude':'-75.94226499999999',
    'Latitude':'45.318620499999994',
    'CurrentPage':'1',
    'ZoomLevel':'7',
    'PropertyTypeGroupID':'1',
    'Token':'',
    'GUID':'',
    'Version':'6.0'
}

kkk = " ApplicationSettings.Token = 'D6TmfZprLI+bju9lrx4jNjGK46lLSsV+jM3lrScYgjc='; ApplicationSettings.GUID = '2417a064-24b2-4cf8-8b85-a00ba018b82b';    "

def postDataToGetPage(loginUrl, postData):
    global session
    session = requests.session()
    session.post(loginUrl, data=postData, headers=Header)
    #print session.get(DOWNLOAD_URL, headers=Header).content
    return session
    
def download_page(url):
    global session
    session = requests.session()
    print url
    return session.get(url, headers=headers, proxies=proxies).content


def parse_html(html):
    global postNumber,publisher, session

    soup = BeautifulSoup(html, "lxml")
    root = soup.find('div', attrs={'class':'discussionList'})
    leaf = root.find('ol', attrs={'class':'discussionListItems'})
    for list in leaf.find_all('li', attrs={'id':re.compile(r'thread-\d+')}):
        _, _, id = list['id'].partition('-')
        url = "http://bbs.comefromchina.com/threads/"+id
        if FILTER and list['data-author'] not in publisher:
            continue
        print "post-------->"+url
        while url:
            html = download_page(url, session)
            url = parse_post(html)
        postNumber = 0    
    next = soup.find('div', attrs={'class':'pageNavLinkGroup'}).find('div',attrs={'class':'PageNav'}).find('a',attrs={'href':re.compile(r'forums/\d+/page-\d+'),'class':'text'}, text="下一页 >")
    return "http://bbs.comefromchina.com/"+next['href']

def parse_mainPage(html):
    global postData
    print html
    #soup = BeautifulSoup(html, "lxml")
    #root = soup.find('head', attrs={'id':'elHead'})
    #print root
    m = re.match(r"ApplicationSettings\.Token = \'(.*?)\'", kkk)
    token = m.groups()[0]
    print token
    n = re.match(r"ApplicationSettings\.GUID", kkk)
    guid = n.groups()[0]
    print guid
    #print root.text

def main():
    global session
    url = DOWNLOAD_URL
    #html = download_page(url)
    parse_mainPage(None) 
'''
    session = postDataToGetPage(loginUrl, postData)

    while url:
        html = download_page(url, session)
        url = parse_html(html)
'''
if __name__ == '__main__':
    main()

