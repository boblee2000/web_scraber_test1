#!/usr/bin/python
#-*-coding:utf-8 -*-

import codecs
import re
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://bbs.comefromchina.com/forums/5/'
index = 2

html = '''
<li id="post-10621681" class="message   " data-author="YINGWA">

	

<div class="messageUserInfo" itemscope="itemscope" itemtype="http://data-vocabulary.org/Person">	
<div class="messageUserBlock ">
	
		<div class="avatarHolder">
			<span class="helper"></span>
			<a href="members/80825/" class="avatar Av80825m" data-avatarhtml="true"><img src="styles/default/xenforo/avatars/avatar_m.png" width="96" height="96" alt="YINGWA"></a>
			
			<!-- slot: message_user_info_avatar -->
		</div>
	


	
		<h3 class="userText">
			<a href="members/80825/" class="username" dir="auto" itemprop="name">YINGWA</a>
			<em class="userTitle" itemprop="title">初级会员</em>
			ID:80825
			
			<!-- slot: message_user_info_text -->
		</h3>
	
		
	
		<div class="extraUserInfo">
			
			
    <dl class="conversationPostBitContainer">
        <a class="OverlayTrigger PopupItemLink" data-cacheoverlay="false" href="posts/10621681/conversation?to=YINGWA">发起悄悄话</a>
    </dl>



				
					<dl class="pairsJustified">
						<dt>注册:</dt>
						<dd>2008-05-01</dd>
					</dl>
				
				
				
					<dl class="pairsJustified">
						<dt>帖子:</dt>
						<dd><a href="search/member?user_id=80825" class="concealed" rel="nofollow">1,123</a></dd>
					</dl>
				
				
				
					<dl class="pairsJustified">
						<dt>支持:</dt>
						<dd>64</dd>
					</dl>
				
				
				
					<dl class="pairsJustified">
						<dt>声望:</dt>
						<dd><a href="members/80825/trophies" class="OverlayTrigger concealed">58</a></dd>
					</dl>
				
			
				
				
				
				
				
			
				
							
			<dl class="pairsInline">
	<dt>金钱:</dt>
	<dd>
		
			<a href="credits/transfer?receiver=YINGWA" class="Tooltip OverlayTrigger concealed" data-cacheoverlay="no" data-userid="80825">$32,461</a>
		
	</dd>
</dl>
				
			
			
			
				
					
				
					
				
					
				
					
				
					
				
					
				
					
				
				
			
			
			
		</div>
	
		


	<span class="arrow"><span></span></span>
</div>
</div>

	<div class="messageInfo primaryContent">
		<strong class="newIndicator"><span></span>新的</strong>
		
		
		
		
		<div class="messageContent">		
			<article>
				<blockquote class="messageText SelectQuoteContainer ugc baseHtml">
					


	






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
				</blockquote>
			</article>
			
		</div>
		
		
		
		
		
		
				
		<div class="messageMeta ToggleTriggerAnchor">
			
			<div class="privateControls">
				
				<span class="item muted">
					<span class="authorEnd"><a href="members/80825/" class="username author" dir="auto">YINGWA</a>,</span>
					<a href="threads/1594329/#post-10621681" title="永久链接" class="datePermalink"><abbr class="DateTime" data-time="1503849232" data-diff="11481" data-datestring="2017-08-27" data-timestring="23:53" title="2017-08-27 ，23:53">昨天 23:53</abbr></a>
				</span>
				
				
				
				
				
				
				
				
				
					<a href="posts/10621681/report" class="OverlayTrigger item control report" data-cacheoverlay="false"><span></span>举报</a>
				
				
				
<a href="posts/10621681/conversation?to=YINGWA" class="OverlayTrigger item control report" data-cacheoverlay="false">发起悄悄话</a>


			</div>
			
			<div class="publicControls">
				<a href="threads/1594329/#post-10621681" title="永久链接" class="item muted postNumber hashPermalink OverlayTrigger" data-href="posts/10621681/permalink">#9</a>
				
				
					<a href="posts/10621681/like" class="LikeLink item control like" data-container="#likes-post-10621681"><span></span><span class="LikeLabel">支持</span></a>
				
				
					<a href="threads/1594329/reply?quote=10621681" data-messageid="10621681" class="MultiQuoteControl JsOnly item control" title="切换多重引用"><span></span><span class="symbol">+</span></a>
					<a href="threads/1594329/reply?quote=10621681" data-posturl="posts/10621681/quote" data-tip="#MQ-10621681" class="ReplyQuote item control reply" title="回复时引用此帖"><span></span>回复</a>
				
				
			</div>
		</div>
	
		
		<div id="likes-post-10621681"></div>
	</div>

	
	
	
</li>
'''

def download_page(url):
    print url
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content


def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    movie_list_soup = soup.find('li', attrs={'id':re.compile('post-\d+'), 'class':re.compile('message\s+')})
    #print movie_list_soup.contents
    #print movie_list_soup.children
    for list in movie_list_soup.children:
        print list
    print movie_list_soup['data-author']
    next = movie_list_soup.find('blockquote', attrs={'class':re.compile('messageText\s+SelectQuoteContainer.*?')})
    for element in next.next_elements:
        print 1
        print element
    #print next.get_text().strip()
    return None
'''
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
'''   



def main():
            url = parse_html(html)

if __name__ == '__main__':
    main()

