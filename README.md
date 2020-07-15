# teleg

Telegram Web Util.

## usage

```
import teleg
teleg.get(channel_name) 
# return Channel object, with channel.title, channel.description, channel.exist
teleg.getPosts(channel_name)
# returns list of Post object, with post.file, post.link, 
# post.preview, post.texts, post.hasLink(), post.id, post.channel, 
# post.key, post.getReferers()
teleg.getPost(channel_name, post_id)
teleg.getPosts(channel_name, post_id) # start from post_id
```

## how to install

`pip3 install teleg`
# teleg
