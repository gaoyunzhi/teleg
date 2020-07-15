#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def testPost(post):
	print(post)
	print(post.getIndex())
	print(post.__dict__)
	print(webgram.getReferer(post))

def test():
	testPost(webgram.get('dushufenxiang'))
	testPost(webgram.getPosts('dushufenxiang', 200))
	testPost(webgram.getPost('dushufenxiang_chat', 200))

if __name__=='__main__':
	test()