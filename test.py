#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def testPost(post):
	print(post.text)
	print()

def test():
	testPost(webgram.getPost('Teahouse2nd', 107940))

if __name__=='__main__':
	test()