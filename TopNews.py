#!/usr/bin/env python
from twython import TwythonStreamer
from twython import Twython

twitter = Twython('SkAhAixhHs2TXyjfcr3OwCDGN', 'tQFLJFjSECi5GF2Fm9GlqZVNk3BHFvxtzeRUHiKqUyLxf6ttFK')
user_timeline = twitter.get_user_timeline(screen_name='@Reuters')

newslist = []


def main():
    for tweet in user_timeline:
        newslist.append(tweet['text'])
        print tweet['text']
    return newslist


if __name__ == "__main__":
    main()


# Streaming

# tweets = []


# class MyStreamer(TwythonStreamer):
#     def on_success(self, data):
#         if 'text' in data:
#             tweets.append(data)
#             print data['text'].encode('utf-8')
#         # if data['lang'] == 'en':
#         #     tweets.append(data)
#         #     print "received tweet #", len(tweets)
#
#         # if len(tweets) >= 20:
#         #     self.disconnect()
#
#     def on_error(self, status_code, data):
#         print status_code, data
#         self.disconnect()
#
# stream = MyStreamer('SkAhAixhHs2TXyjfcr3OwCDGN',
#                     'tQFLJFjSECi5GF2Fm9GlqZVNk3BHFvxtzeRUHiKqUyLxf6ttFK',
#                     '3950603013-S2ueAgrrL3hgxsC2COOwHwpdCBVeyHiB0fI3rVB',
#                     'fQIviIGSxLWGtB0DbabmEdwXa9zUPlG5f4Xg1mAluVjYx')