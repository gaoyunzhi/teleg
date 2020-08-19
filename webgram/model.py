from .ssoup import getField, getTime, getForwardFrom, getLinks, isGroup, getAFieldSuffix
from .util import getText, cutText, textJoin

def isValidName(candidate):
	if len(candidate) > 40:
		return False
	for c in '?#=!%,.':
		if c in candidate:
			return False
	return True

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
				if len(parts) <= 1:
					continue
				candidate = parts[1]
				if isValidName(candidate):
					yield candidate

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
			return getText(self.file, self.link, self.preview, 
				self.text, self.poll)
		textLink = None
		for item in self.text.find_all('a'):
			textLink = getText(item)
			if textLink:
				break
		if not textLink:
			return getText(self.file, self.link, self.preview, self.text)
		text = getText(self.text)
		first_part = text.split(textLink)[0]
		second_part = text[len(first_part):]
		return textJoin(getText(self.file), first_part, 
			getText(self.link, self.preview), second_part)

	def getIndex(self):
		raw = []
		if self.isChannel():
			if self.is_group:
				raw.append('isGroup')
		else:
			if len(getLinks(self.text)) > 0:
				raw.append('hasLink')
			if self.file:
				raw.append('hasFile')
			if self.poll:
				raw.append('hasPoll')
			if self.author or getText(self.author_field):
				raw.append('hasAuthor')
		raw += [self.forward_from, self.author, self.reply, 
			self.forward_author, getText(self.author_field), 
			self._getIndex()]
		return ' '.join([x for x in raw if x])

	def getKey(self):
		return '%s/%d' % (self.channel, self.post_id)

	def yieldPhotos(self):
		for item in self.soup.find_all('a', class_='tgme_widget_message_photo_wrap'):
			yield item['style'].split("background-image:url('")[1].split("')")[0]

	def __str__(self):
		return '%s: %s' % (self.getKey(), self.getMaintext())

def getPostFromSoup(name, soup):
	post = Post(name)
	post.soup = soup
	post.title = getField(soup, 'tgme_page_title', 
		'tgme_channel_info_header_title')
	post.description = getField(soup, 'tgme_page_description',
		'tgme_channel_info_description')
	post.reply = getAFieldSuffix(soup, 'tgme_widget_message_reply')
	reply_quote = soup.find('a', class_='tgme_widget_message_reply')
	if reply_quote:
		reply_quote.decompose()
	post.link = getField(soup, 'link_preview_title')
	post.file = getField(soup, 'tgme_widget_message_document_title')
	post.text = getField(soup, 'tgme_widget_message_text')
	post.poll = getField(soup, 'tgme_widget_message_poll')
	post.preview = getField(soup, 'link_preview_description')
	post.time = getTime(soup)
	post.forward_from = getForwardFrom(soup)
	post.author = getAFieldSuffix(soup, 'tgme_widget_message_author_name')
	post.author_field = soup.find('span', 'tgme_widget_message_author_name')
	post.forward_author = getAFieldSuffix(soup, 
		'tgme_widget_message_forwarded_from_name')
	post.is_group = isGroup(soup)
	return post
	