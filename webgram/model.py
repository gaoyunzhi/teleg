from .soup import getField
from .util import getTime, getForwardFrom

def Item(object):
	def __init__(self, channel):
		self.channel = channel
		self.post_id = 0
		self.exist = True

	def getLinks(self):
		if not self.text:
			return []
		return [item['href'] for item in 
			self.text.find_all('a') if 'href' in item]

	# def __str__(self):
	# 	to_print = [('name')]
	# 	return 'name: %s, title: %s, exist: %s' % (
	# 		self.name, getText(self.title), str(self.exist)) 

def getItemFromSoup(name, soup):
	item = Item(name)
	item.title = getField(soup, 'tgme_page_title', 
		'tgme_channel_info_header_title')
	item.description = getField(soup, 'tgme_page_description',
		'tgme_channel_info_description')
	item.link = getField(soup, 'link_preview_title')
	item.file = getField(soup, 'tgme_widget_message_document_title')
	item.text = getField(soup, 'tgme_widget_message_text')
	item.preview = getField(soup, 'link_preview_description')
	item.time = getTime(soup)
	item.forward_from = getForwardFrom(soup)