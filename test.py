#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import teleg

def test():
	print(teleg.get('dushufenxiang'))
	print(teleg.getPosts('dushufenxiang', 200))
	print(teleg.getPost('dushufenxiang_chat', 200))

if __name__=='__main__':
	test()