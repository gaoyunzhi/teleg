#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'webgram'
import cached_url
from bs4 import BeautifulSoup

def getText(item):
	if not item:
		return ''
	return item.text

def Item(object):
	def __init__(self, channel, post_id=0, text=None, file=None, 
		link=None, preview=None, title=None, description=None, exist=True):
		self.channel = channel
		self.post_id = post_id
		self.text = text
		self.file = file
		self.link = link
		self.preview = preview
		self.name = name
		self.title = title
		self.description = description
		# for user and bot, title will exist, exist will be false
		self.exist = exist 

	def __str__(self):
		to_print = [('name')]
		return 'name: %s, title: %s, exist: %s' % (
			self.name, getText(self.title), str(self.exist)) 


def getReferer(soup):
	...

def _getButtonText(soup):
	item = soup.find('a', class_='tgme_action_button_new')
	return item and item.text

def get(name):
	link = 'https://t.me/' + name
	content = cached_url.get(link, force_cache=True)
	if 'tgme_page_title' not in content:
		return Item(name, exist=False)
	soup = BeautifulSoup(content, 'html.parser')
	title = soup.find('div', class_='tgme_page_title')
	description = soup.find('div', class_='tgme_page_description')
	exist = 'Send Message' not in _getButtonText(soup)
	return Item(name, text = title, 
		description = description, exist = exist)

