from .ssoup import getField, getTime, getForwardFrom, getLinks
from .util import getText, cutText, textJoin

class Post(object): # can be a post or channel info wrap
	def __init__(self, channel):
		self.channel = channel
		self.post_id = 0
		self.exist = True

	def yieldRefers(self):
		if self.forward_from:
			yield self.forward_from
		soup = self.description if self.isChannel() else self.text
		for link in getLinks(soup):
			if 't.me' in link:
				parts = link.split('t.me')[-1].split('/')
				if len(parts) > 1:
					yield parts[1]

	def isChannel(self):
		return self.post_id == 0

	def getMaintext(self, cut = 20, channel_cut = 15):
		if self.isChannel():
			return cutText(getText(self.title), channel_cut)
		return cutText(self._getIndex(), cut)

	def _getIndex(self):
		if self.isChannel():
			return getText(self.title, self.description)
		if not self.text or not self.link:
			return getText(self.file, self.link, self.preview, self.text)
		textLink = getText(self.text.find('a'))
		text = getText(self.text)
		first_part = text.split(textLink)[0]
		second_part = text[len(first_part):]
		return textJoin(getText(self.file), first_part, 
			getText(self.link, self.preview), second_part)

	def getIndex(self):
		raw = []
		if len(getLinks(self.text)) > 0:
			raw.append('hasLink')
		if self.file:
			raw.append('hasFile')
		raw.append(self._getIndex())
		return ' '.join(raw)

	def getKey(self):
		return '%s/%d' % (self.channel, self.post_id)

	def __str__(self):
		return '%s: %s' % (self.getKey(), self.getMaintext())

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
	return post
	