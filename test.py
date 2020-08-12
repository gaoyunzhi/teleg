#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def testPost(post):
	index = post.getIndex()
	if index:
		print(index + '\n')

def test():
	[testPost(post) for post in webgram.getPosts('douban_read')]

if __name__=='__main__':
	test()