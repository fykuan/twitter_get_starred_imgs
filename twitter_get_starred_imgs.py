#!/usr/bin/env python
# -*- coding:utf8 -*-
import argparse
import datetime
import json
import re
import sys
import twitter
import urllib2
import os

def main(args):
    dropbox_dir = None

    parser = argparse.ArgumentParser(description="Save images with starred")
    parser.add_argument("-c", "--config", type=argparse.FileType('r'))
    parser.add_argument("-d", "--dropbox", action="store", type=str)
    arguments = parser.parse_args(args)

    if hasattr(arguments, 'dropbox'):
        dropbox_dir = arguments.dropbox

    twitter_creditentials = json.loads(arguments.config.read())

    twitter_api = twitter.Api(
        consumer_key = twitter_creditentials["CONSUMER_KEY"],
        consumer_secret = twitter_creditentials["CONSUMER_SECRET"],
        access_token_key = twitter_creditentials["ACCESS_TOKEN"],
        access_token_secret = twitter_creditentials["ACCESS_TOKEN_SECRET"])

    favs = twitter_api.GetFavorites()
    image_list = []

    for fav in favs:
        try:
            for media in fav.media:
                image_list.append(media['media_url'])
        except Exception as e:
            print e

    for url in image_list:
        data = urllib2.urlopen(url)
        match = re.findall(r"http://.*?/media/(.*)", url)
        filename = match[0]
        if not os.path.isfile(filename):
            if dropbox_dir != None:
                try:
                    outputfile = open("%s/twitter_get_starred_imgs/%s" % (dropbox_dir, filename), "wb")
                    print "Saving %s to %s" % (filename, dropbox_dir)
                    outputfile.write(data.read())
                    outputfile.close()
                except Exception as e:
                    print e
            else:
                try:
                    outputfile = open("%s" % (filename), "wb")
                    print "Saving %s" % (filename)
                    outputfile.write(data.read())
                    outputfile.close()
                except Exception as e:
                    print e
        else:
            print "%s already exists" % (filename)

if __name__ == "__main__":
    main(sys.argv[1:])