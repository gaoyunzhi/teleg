#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'webgram'
from .ssoup import getSoup, getPostId
from .model import Post, getPostFromSoup

def _yieldPosts(name, soup):
	post = getPostFromSoup(name, soup)
	yield post
	for sub_soup in soup.find_all('div', class_='tgme_widget_message_bubble'):
		post = getPostFromSoup(name, sub_soup)
		post.post_id = getPostId(sub_soup)
		yield post

def _getPostsSoup(name, post_id=None):
	link = 'https://t.me/s/' + name
	if post_id:
		link += '/' + str(post_id)
	return getSoup(link, force_cache=(not post_id))

def getPosts(name, post_id=None):
	soup = _getPostsSoup(name, post_id = post_id)
	return list(_yieldPosts(name, soup))

def getPost(name, post_id):
	soup = getSoup('https://t.me/%s/%d?embed=1' % (name, post_id))
	post = getPostFromSoup(name, soup)
	post.post_id = post_id
	return post

def get(name):
	soup = getSoup('https://t.me/' + name)
	post = getPostFromSoup(name, soup)
	if not post.title or 'Send Message' in str(
		soup.find('a', class_='tgme_action_button_new')):
		post.exist = False
	return post

def yieldReferers(post):
	for name in post.yieldRefers():
		if get(name).exist:
			yield name

