#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def testPost(post):
	# print(post)
	# print(post.getIndex())
	# print(post.getMaintext())
	print(post.getKey())
	# print(post.__dict__)
	# print(list(webgram.yieldReferers(post)))
	# list(webgram.yieldReferers(post))

def test():
	# testPost(webgram.get('freedom_watch'))
	# [testPost(post) for post in webgram.getPosts('equality_and_rights', 1142)]
	# testPost(webgram.getPost('equality_and_rights', 6371))
	[testPost(post) for post in webgram.getPosts('Pinwan', 100000, direction='after', force_cache=True)]
	# [testPost(post) for post in webgram.getPosts('freedom_watch')]
	# print(len(webgram.getPosts('Pinwan', 100000, direction='after')))

if __name__=='__main__':
	test()