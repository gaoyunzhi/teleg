#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

# not use telegram_util once, because that one mess up with markdown
# also, this way reduce dependency
def cutText(text, cut):
	if len(text) <= cut + 3:
		return text
	return text[:cut] + '...'

def getText(*soups):
	result = []
	for soup in soups:
		if soup:
			result.append(' '.join(soup.text.strip().split()))
	return ' '.join(result)