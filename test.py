#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 22:13:36 2018

@author: samarth
"""

import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import re

"# -- coding: utf-8 --"


def calctime(a):
    return time.time() - a


positive = 0
negative = 0
compound = 0

count = 0
initime = time.time()
plt.ion()

import test

ckey = "hDCLHAFieKH2o19OmDMNPlttg"
csecret = "3cvWKDWxLYB0aN7sjYvudIBMhYz9ES4XoOGbxeqnjePLUpuaFh"
atoken = "888388700949757952-MXe8Y9qXiod4EFZ2c2UlHVZCvBSzYo4"
asecret = "orx8rRp955Hk6n8aLD18DduBUTWpkuH0y8P33B5HUquSs"


class listener(StreamListener):

    def on_data(self, data):
        global initime
        t = int(calctime(initime))
        all_data = json.loads(data)
        tweet = all_data["text"]
        # username=all_data["user"]["screen_name"]
        tweet = " ".join(re.findall("[a-zA-Z]+", tweet))
        blob = TextBlob(tweet.strip())

        global positive
        global negative
        global compound
        global count

        count = count + 1
        senti = 0
        for sen in blob.sentences:
            senti = senti + sen.sentiment.polarity
            if sen.sentiment.polarity >= 0:
                positive = positive + sen.sentiment.polarity
            else:
                negative = negative + sen.sentiment.polarity
        compound = compound + senti
        print(count)
        print(tweet.strip())
        print(senti)
        print(t)
        print(str(positive) + ' ' + str(negative) + ' ' + str(compound))

        plt.axis([0, 70, -20, 20])
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.plot([t], [positive], 'go', [t], [negative], 'ro', [t], [compound], 'bo')
        plt.show()
        plt.pause(0.0001)
        # if count == 200:
        #    return False
        # else:
        #    return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener(count))
twitterStream.filter(track=["Kim Jong"])
