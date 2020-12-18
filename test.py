#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def test():
	print(webgram.getPost('douban_read', 38353).getVideo())

if __name__=='__main__':
	test()