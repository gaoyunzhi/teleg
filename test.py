#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def testPost(post):
	# print(post)
	print(post.getIndex())
	print(post.getMaintext())
	print(post.getKey())
	# print(post.__dict__)
	# print(list(webgram.yieldReferers(post)))

def test():
	# testPost(webgram.get('freedom_watch'))
	# [testPost(post) for post in webgram.getPosts('dushufenxiang', 1142)]
	# testPost(webgram.getPost('dushufenxiang', 1142))
	testPost(webgram.getPosts('dushufenxiang', 1142)[2])
	# [testPost(post) for post in webgram.getPosts('freedom_watch')]

if __name__=='__main__':
	test()