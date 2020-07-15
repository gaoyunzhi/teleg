#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def testPost(post):
	print(post)
	print(post.getIndex())
	print(post.__dict__)
	print(list(webgram.yieldReferers(post)))

def test():
	testPost(webgram.get('dushufenxiang'))
	[testPost(post) for post in webgram.getPosts('dushufenxiang', 200)]
	testPost(webgram.getPost('dushufenxiang_chat', 200))
	[testPost(post) for post in webgram.getPosts('dushufenxiang')]

if __name__=='__main__':
	test()