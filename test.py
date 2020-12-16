#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def testPost(post):
	print(post.getAuthor())

def test():
	testPost(webgram.get('MadLadMemes'))

if __name__=='__main__':
	test()