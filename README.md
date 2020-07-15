# webgram

Telegram Web Util.

## usage

```
import webgram
webgram.get(channel_name) 
# return Channel object, with channel.title, channel.description, channel.exist
webgram.getPosts(channel_name)
# returns list of Post object, with post.file, post.link, 
# post.preview, post.text, post.hasLink(), post.id, post.channel, 
# post.getReferers()
webgram.getPost(channel_name, post_id)
webgram.getPosts(channel_name, post_id) # start from post_id
```

## how to install

`pip3 install webgram`
# webgram
