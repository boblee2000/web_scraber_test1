#!/usr/bin/python
#-*-coding:utf-8 -*-

import json
import codecs
import re
import requests
from bs4 import BeautifulSoup
import http
import random
import time

DOWNLOAD_URL = 'https://www.realtor.ca/'
FILTER = 1
postNumber = 0
publisher = ['deepthroat']
poster = ['deepthroat']

Cookie = {
    "__qca":"P0-790114168-1501392557222", "__utma":"151806763.485722766.1501392556.1503617627.1503623980.2", "__utmc":"151806763", "__utmz":"151806763.1503623980.2.2.utmcsr=bbs.comefromchina.com|utmccn=(referral)|utmcmd=referral|utmcct=/threads/880733/page-4", "xfa_user":"127809%2Ca2949cb8acf1b54363ceb0a9d3f78fb6f517f966", "xfa_session":"8e5844c7732e0e69922da55d811b0099", "_ga":"GA1.2.485722766.1501392556", "_gid":"GA1.2.1655723088.1504142767", "_gat":'1', "__asc":"0a6bbb3b15e4f66d58612d00be2", "__auc":"e76f6d0b15d91f852c2d2c6b194"
}

proxies = {"https": "123.0.213.100:80", "https": "124.158.124.237:65103", "https": "124.81.234.124:8080", "https": "124.152.84.65:53281", "https": "123.180.133.42:8118", "https":"125.25.55.188:8080"}  


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
    'LongitudeMin':'-76.10138258109129',
    'LongitudeMax':'-75.71033796439207',
    'LatitudeMin':'45.220726108171895',
    'LatitudeMax':'45.40566522481841',
    'SortOrder':'A',
    'SortBy':'1',
    'viewState':'m',
    'Longitude':'-75.94229539999999',
    'Latitude':'45.318612599999994',
    'CurrentPage':'1',
    'ZoomLevel':'7',
    'PropertyTypeGroupID':'1',
    'Token':'',
    'GUID':'',
    'Version':'6.0'
}


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
    print soup
    root = soup.find('div', attrs={'class':'m_map'}).find('div', attrs={'id':'listView'})
    for list in root.find_all('div', attrs={'class':'m_property_lst_row'}):
        print list.text
    return None

def parse_mainPage(html):
    soup = BeautifulSoup(html, "lxml")
    root = soup.find('head', attrs={'id':'elHead'})
    keyList = re.findall(r"ApplicationSettings\.(?P<name>\w+) = \'(?P<value>.*?)\'", root.text)
    keyDict = dict(keyList)
    print keyDict, '\n\n\n'
    return keyDict

def main():
    global session,postData
    url = DOWNLOAD_URL
    html = download_page(url)
    #print html
    keyDict = parse_mainPage(html) 
    postData['Token']=keyDict['Token']
    postData['GUID']=keyDict['GUID']
    #print postData
        
    while postData:
        html = session.post(loginUrl, data=postData, headers=headers)
        if not html: break
                
        kk = json.loads(html.text)
        print kk['Paging']
        currentPage = kk['Paging']['CurrentPage']
        totalPages = kk['Paging']['TotalPages']
        
        postData['CurrentPage']= str(currentPage + 1)
        print postData['CurrentPage']
        if currentPage >= totalPages:
            postData = None
        time.sleep(3)        
        #postData = parse_html(html)

if __name__ == '__main__':
    main()

