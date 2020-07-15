#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'webgram'
from .util import getPostId
from .soup import getSoup
from .model import Item, getItemFromSoup

def _yieldPosts(name, soup):
	yield getItemFromSoup(name, soup)
	for sub_soup in soup.find_all('div', class_='tgme_widget_message_bubble'):
		item = getItemFromSoup(name, sub_soup)
		item.post_id = getPostId(sub_soup)

def _getPostsSoup(name, post_id=None):
	link = 'https://t.me/s/' + name
	if post_id:
		link += '/' + str(post_id)
	return getSoup(link, force_cache=(not post_id))

def getPosts(name, post_id=None):
	soup = _getPostsSoup(name, post_id = post_id)
	return list(_yieldPosts(name, soup))

def getPost(name, post_id):
	soup = getSoup('https://t.me/%s/%d' % (name, post_id))
	item = getItemFromSoup(name, soup)
	item.post_id = post_id
	return item

def getReferer(soup):
	...

def get(name):
	item = getItemFromSoup(name, getSoup('https://t.me/' + name))
	if not item.title or 'Send Message' in str(
		soup.find('a', class_='tgme_action_button_new')):
		self.exist = False
	return item

