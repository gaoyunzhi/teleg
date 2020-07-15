#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

# not use telegram_util once, because that one mess up with markdown
# also, this way reduce dependency
def cutText(text, cut):
	if len(text) <= cut + 3:
		return text
	return text[:cut] + '...'

def getText(*soups):
	result = []
	for soup in soups:
		if soup:
			result.append(' '.join(soup.text.strip().split()))
	return ' '.join(result)

def getTime(soup):
	try:
		return datetime.strptime(soup.find('a', 
			class_='tgme_widget_message_date').find('time')[
			'datetime'][:-6], '%Y-%m-%dT%H:%M:%S').timestamp()
	except:
		return 0

def getPostId(soup):
	post_link = soup.find('a', 
		class_='tgme_widget_message_date')['href']
	return int(post_link.split('/')[-1])

def getForwardFrom(soup):
	try:
		result = item.find('a', class_=
			'tgme_widget_message_forwarded_from_name')['href']
		result = result.split('/')
		int(result[-1])
		return result[-2]
	except:
		...

def getLinks(soup):
	if not soup:
		return []
	return [item['href'] for item in 
		soup.find_all('a') if item.get('href')]
	