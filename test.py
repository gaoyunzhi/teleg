#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def test():
	print(webgram.get('dushufenxiang'))
	print(webgram.getPosts('dushufenxiang', 200))
	print(webgram.getPost('dushufenxiang_chat', 200))

if __name__=='__main__':
	test()