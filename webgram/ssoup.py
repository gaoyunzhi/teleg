import cached_url
from bs4 import BeautifulSoup
from datetime import datetime

def getSoup(url, force_cache=True):
	return BeautifulSoup(cached_url.get(url, force_cache=True),
		'html.parser')

def getField(soup, *fields):
	for field in fields:
		result = soup.find('div', class_=field)
		if result:
			return result

def getForwardFrom(soup):
	try:
		result = soup.find('a', class_=
			'tgme_widget_message_forwarded_from_name')['href']
		result = result.split('/')
		int(result[-1])
		return result[-2]
	except:
		...

def getTime(soup):
	try:
		return int(datetime.strptime(soup.find('a', 
			class_='tgme_widget_message_date').find('time')[
			'datetime'][:-6], '%Y-%m-%dT%H:%M:%S').timestamp())
	except:
		return 0

def getPostId(soup):
	post_link = soup.find('a', 
		class_='tgme_widget_message_date')['href']
	return int(post_link.split('/')[-1])

def getLinks(soup):
	if not soup:
		return []
	return [item['href'] for item in 
		soup.find_all('a') if item.get('href')]
	