#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def testPost(post):
	index = post.getIndex()
	if index:
		print(index + '\n')

def test():
	# [testPost(post) for post in webgram.getPosts('muddycat', 67, direction='after')]
	for post_id in range(107900, 107941):
		testPost(webgram.getPost('Teahouse2nd', post_id))

if __name__=='__main__':
	test()