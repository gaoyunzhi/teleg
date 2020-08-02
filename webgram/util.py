#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

# not use telegram_util once, because that one mess up with markdown
# also, this way reduce dependency
def cutText(text, cut):
	if len(text) <= cut + 3:
		return text
	return text[:cut] + '...'

def textJoin(*parts):
	result = ' '.join(parts)
	parts = [x for x in result.split() if x]
	return ' '.join(parts)

def getText(*soups):
	result = []
	for soup in soups:
		if soup:
			for br in soup.find_all("br"):
				br.replace_with("\n")
			result.append(soup.text)
	return textJoin(*result)