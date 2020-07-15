import cached_url
from bs4 import BeautifulSoup

def getSoup(url, force_cache=True):
	return BeautifulSoup(cached_url.get(link, force_cache=True),
		'html.parser')

def getField(soup, *fields):
	for field in fields:
		result = soup.find('div', class_=field)
		if result:
			return result