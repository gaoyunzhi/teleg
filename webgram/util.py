#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

def getText(item, cut=-1):
	if not item:
		return ''
	result = ' '.join(item.text.strip().split())
	return result[:cut]

def getTime(item):
	try:
		return datetime.strptime(item.find('a', 
			class_='tgme_widget_message_date').find('time')[
			'datetime'][:-6], '%Y-%m-%dT%H:%M:%S').timestamp()
	except:
		return 0

def getPostId(soup):
	post_link = soup.find('a', 
		class_='tgme_widget_message_date')['href']
	return int(post_link.split('/')[-1])