#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/30 21:04:31 Shin Kanouchi

import argparse
import json
from StringIO import StringIO


def get_country_text(my_file, country_name):
    uni_country_name = unicode(country_name,'utf-8')
    for line in open(my_file):
        jdata = json.load(StringIO(line))
        #print json.dumps(jdata, sort_keys = True, indent = 4, ensure_ascii=False)
        if jdata['title'] == uni_country_name:
            return jdata['text']


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default="../data/jawiki-country.json", help='input training data')
    parser.add_argument('-c', '--country', dest='country', default='イギリス', help='input training data')
    args = parser.parse_args()
    print get_country_text(args.train, args.country)