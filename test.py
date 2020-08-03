#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def testPost(post):
	print(post.getIndex())
	print()

def test():
	testPost(webgram.getPost('equality_and_rights', 6371))
	testPost(webgram.getPosts('Pinwan', force_cache=True)[0])
	testPost(webgram.getPosts('dushufenxiang_chat', force_cache=True)[0])
	testPost(webgram.get('dushufenxiang_chat'))
	testPost(webgram.get('dushufenxiang'))

if __name__=='__main__':
	test()