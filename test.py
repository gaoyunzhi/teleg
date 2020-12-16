#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def testPost(post):
	print(post.getAuthor())

def test():
	for post_id in range(41991, 41992):
		testPost(webgram.getPost('douban_discuss', post_id))

if __name__=='__main__':
	test()