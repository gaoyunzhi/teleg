#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import weiboo
import time

def testSearch(key):
	for url, card in weiboo.search(key):
		print(url, weiboo.getCount(card))
	with open('tmp.txt', 'w') as f:
		f.write(str(weiboo.search(key)))

def testSearchUser(key):
	print(weiboo.searchUser(key))
	time.sleep(10)

if __name__=='__main__':
	testSearch('女权')
	testSearch('6520732164')
	testSearchUser('澎湃新闻')
	testSearchUser('5044281310')