#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def testPost(post):
	print(post.getIndex())
	print()

def test():
	[testPost(post) for post in webgram.getPosts('dushufenxiang')]

if __name__=='__main__':
	test()