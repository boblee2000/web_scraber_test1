#!/usr/bin/python
#-*-coding:utf-8 -*-

import codecs
import re
import requests
from bs4 import BeautifulSoup
import http


DOWNLOAD_URL = 'http://bbs.comefromchina.com/forums/5/'
FILTER = 1
postNumber = 0
publisher = ['deepthroat']
poster = ['deepthroat']

Cookie = {
    "__qca":"P0-790114168-1501392557222", "__utma":"151806763.485722766.1501392556.1503617627.1503623980.2", "__utmc":"151806763", "__utmz":"151806763.1503623980.2.2.utmcsr=bbs.comefromchina.com|utmccn=(referral)|utmcmd=referral|utmcct=/threads/880733/page-4", "xfa_user":"127809%2Ca2949cb8acf1b54363ceb0a9d3f78fb6f517f966", "xfa_session":"8e5844c7732e0e69922da55d811b0099", "_ga":"GA1.2.485722766.1501392556", "_gid":"GA1.2.1655723088.1504142767", "_gat":'1', "__asc":"0a6bbb3b15e4f66d58612d00be2", "__auc":"e76f6d0b15d91f852c2d2c6b194"
}

Header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}


session = None

loginUrl = 'http://bbs.comefromchina.com/login/login'
postData = {
    'login':'jenkins',
    'register':'0',
    'password':'5418854188@Oco',
    'remember':'0',
    'cookie_check':'0',
    'redirect':'/',
    '_xfToken':''
}

def loginByCookie():
    session = requests.session()
    session.cookies = http.cookiejar.LWPCookieJar(filename='cookies.txt')
    try:
        print(session.cookies)
        session.cookies.load(ignore_discard=True)
    except:
        print("还没有cookie信息 we need to login using username/password")
    return session

def loginByUsernamePassword(loginUrl, postData):
    session = requests.session()
    session.post(loginUrl, data=postData, headers=Header)
    #print session.get(DOWNLOAD_URL, headers=Header).content
    return session
    
def download_page(url, session):
    print url
    return session.get(url, headers=Header).content

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

def main():
    global session
    url = DOWNLOAD_URL
    session = loginByUsernamePassword(loginUrl, postData)

    while url:
        html = download_page(url, session)
        url = parse_html(html)

if __name__ == '__main__':
    main()

