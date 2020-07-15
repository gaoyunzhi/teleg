from .soup import getField, getText, cutText
from .util import getTime, getForwardFrom

def Post(object): # can be a post or channel info wrap
	def __init__(self, channel):
		self.channel = channel
		self.post_id = 0
		self.exist = True

	def _getLinks(self):
		if not self.text:
			return []
		return [item['href'] for item in 
			self.text.find_all('a') if 'href' in item]

	def yieldRefers(self):
		if self.forward_from:
			yield self.forward_from
		for link in self._getLinks():
			if 't.me' in link:
				yield link.split('t.me')[-1].split('/')[0]

	def isChannel(self):
		return self.post_id == 0

	def _getMaintext(self):
		if self.isChannel():
			return getText(self.title)
		return getText(self.file, self.link, self.text)

	def getMaintext(self, cut = 20, channel_cut = 15):
		if self.isChannel():
			cut = channel_cut
		return cutText(self._getMaintext(), cut)

	def _getIndex(self):
		if self.isChannel()
			return getText(self.title, self.description)
		return getText(self.file, self.link, self.preview, self.text)

	def getIndex(self):
		raw = []
		if len(self.getLink()) > 0:
			raw.append('hasLink')
		if self.file:
			raw.append('hasFile')
		raw.append(_getIndex(self))
		return ' '.join(raw)

	def getKey(self):
		return '%s/%d' % (self.channel, self.post_id)

	def __str__(self):
		to_print = [('name')]
		return 'name: %s, title: %s, exist: %s' % (
			self.name, getText(self.title), str(self.exist)) 

def getPostFromSoup(name, soup):
	post = Post(name)
	post.title = getField(soup, 'tgme_page_title', 
		'tgme_channel_info_header_title')
	post.description = getField(soup, 'tgme_page_description',
		'tgme_channel_info_description')
	post.link = getField(soup, 'link_preview_title')
	post.file = getField(soup, 'tgme_widget_message_document_title')
	post.text = getField(soup, 'tgme_widget_message_text')
	post.preview = getField(soup, 'link_preview_description')
	post.time = getTime(soup)
	post.forward_from = getForwardFrom(soup)