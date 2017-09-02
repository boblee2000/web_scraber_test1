#!/usr/bin/env python
# encoding=utf-8

"""
爬取豆瓣电影TOP250 - 完整示例代码
"""

import codecs

import requests
from bs4 import BeautifulSoup, element
import re

DOWNLOAD_URL = 'http://movie.douban.com/top250/'
htmlContent = '''<blockquote class="messageText SelectQuoteContainer ugc baseHtml">
					


	






					<div class="bbCodeBlock bbCodeQuote" data-author="ottawa_tj">
	<aside>
		
			<div class="attribution type">作者: ottawa_tj:
				
					<a href="goto/post?id=10621579#post-10621579" class="AttributionLink">↑</a>
				
			</div>
		
		<blockquote class="quoteContainer"><div class="quote">村长推荐subaru。<br>
<br>
不过看到路上有人开宝马X1，不知多少钱？<br>
虽然是1系列，好歹也是宝马。</div><div class="quoteExpand">点击展开...</div></blockquote>
	</aside>
</div><a href="http://driving.ca/auto-shows/toronto-cias/2017-volkswagen-golf-alltrack-is-canadas-car-of-the-year" target="_blank" class="externalLink ProxyLink" data-proxy-href="proxy.php?link=http%3A%2F%2Fdriving.ca%2Fauto-shows%2Ftoronto-cias%2F2017-volkswagen-golf-alltrack-is-canadas-car-of-the-year&amp;hash=e68f6606086e08294ef5c2a91855df5e" rel="nofollow">http://driving.ca/auto-shows/toronto-cias/2017-volkswagen-golf-alltrack-is-canadas-car-of-the-year</a><br>
<br>
Along with the Car of the Year, AJAC named the refreshed 2017 <a href="http://driving.ca/subaru/forester/" target="_blank" class="externalLink ProxyLink" data-proxy-href="proxy.php?link=http%3A%2F%2Fdriving.ca%2Fsubaru%2Fforester%2F&amp;hash=9a5c93b3319d021038fdfacc6eda5aa7" rel="nofollow">Subaru Forester</a> as this year’s Utility Vehicle of the Year.
					<div class="messageTextEndMarker">&nbsp;</div>
				</blockquote>'''


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content


def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    movie_list_soup = soup.find('blockquote', attrs={'class':re.compile('messageText\s+SelectQuoteContainer.*?')})
    for child in movie_list_soup.children:
        if isinstance(child.next_sibling, element.NavigableString):
            print child.next_sibling
    ##print movie_list_soup.prettify()
    return None
    
"""
    movie_name_list = []

    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs={'class': 'hd'})
        movie_name = detail.find('span', attrs={'class': 'title'}).getText()

        movie_name_list.append(movie_name)

    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return movie_name_list, DOWNLOAD_URL + next_page['href']
    return movie_name_list, None
"""

def main():
    url = DOWNLOAD_URL

    ##with codecs.open('movies', 'wb', encoding='utf-8') as fp:
       ## while url:
            ##html = download_page(url)
    parse_html(htmlContent)
            ##fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))


if __name__ == '__main__':
    main()
