# webgram

Telegram Web Util.

## usage

```
import webgram
webgram.get(channel_name) 
# return Webgram object, with title, description, exist
webgram.getPosts(channel_name)
# returns list of Webgram object, with file, link, 
# preview, text, post.hasLink(), id, channel
# The first object is channel info
webgram.getPost(channel_name, post_id)
webgram.getPosts(channel_name, post_id) # start from post_id
```

## how to install

`pip3 install webgram`
# webgram
