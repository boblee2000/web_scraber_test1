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


def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    movie_list_soup = soup.find('ol', attrs={'class': 'discussionListItems'})

    ##user_title = []
    ##movie_name_list = []

    for movie_li in movie_list_soup.find_all('li'):
        movie_name_list = []
        print movie_li['data-author']
        ##movie_name_list.append(movie_li['data-author'])
        detail = movie_li.find('div', attrs={'class': 'listBlock main'})
        title = detail.find('h3', attrs={'class': 'title'})
        print title.a.get_text()
        ##movie_name_list.append(title.a.get_text())
        ##print movie_name_list


    next_page = soup.find('div', attrs={'class':'pageNavLinkGroup'}).find('a', attrs={'href':re.compile('forums/\d/page-\d+'), 'class':'text'}, text="下一页 >")
    ##for kkk in next_page.find_all('a', attrs={'href':re.compile('forums/\d/page-\d+'), 'class':'text'}):
    print next_page['href']
    if next_page:
        return 'http://bbs.comefromchina.com/' + next_page['href']
    ##return 'http://bbs.comefromchina.com/forums/5/page-' + str(index)
    return None

def parse_html2(html):
    soup = BeautifulSoup(html, "lxml")
    movie_list_soup = soup.find('ol', attrs={'class': 'discussionListItems'})

    ##user_title = []
    ##movie_name_list = []

    for movie_li in movie_list_soup.find_all('li'):
        movie_name_list = []
        print movie_li['data-author']
        ##movie_name_list.append(movie_li['data-author'])
        detail = movie_li.find('div', attrs={'class': 'listBlock main'})
        title = detail.find('h3', attrs={'class': 'title'})
        print title.a.get_text()
        ##movie_name_list.append(title.a.get_text())
        ##print movie_name_list


    next_page = soup.find('div', attrs={'class':'pageNavLinkGroup'}).find('a', attrs={'href':re.compile('forums/\d/page-\d+'), 'class':'text'}, text="下一页 >")
    ##for kkk in next_page.find_all('a', attrs={'href':re.compile('forums/\d/page-\d+'), 'class':'text'}):
    print next_page['href']
    if next_page:
        return 'http://bbs.comefromchina.com/' + next_page['href']
    ##return 'http://bbs.comefromchina.com/forums/5/page-' + str(index)
    return None


def main():
    url = DOWNLOAD_URL
    global index
    with codecs.open('movies', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            url = parse_html(html)
            index += 1
            ##fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))


if __name__ == '__main__':
    main()

