#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'teleg'
import cached_url

class Channel():
	def __init__(self, name, title, description, exist):
		self.name = name
		self.title = title
		self.description = description
		# for user and bot, title will exist, exist will be false
		self.exist = exist 

	def __str__(self):
		return 'name: %s, title: %s, exist: %s' % (
			self.name, self.title, str(self.exist))  

def getReferer()

def get(name):
	...