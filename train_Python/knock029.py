#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/03 17:48:39 Shin Kanouchi

import argparse
import knock020
import knock025
import re
import json
import urllib


def main(info_dic):
    infobox = dict([(key, value.replace("'''''", "").replace("'''", "").replace("''", "")) for key, value in info_dic.items()])
    infobox = dict([(key, re.sub(r"\[\[.*\]\]", lambda x: x.group().replace("[[", "").replace("]]", "").split("|")[0].split("#")[0], value)) for key, value in infobox.items()])
    infobox = dict([(key, re.sub(r"{{.*}}", lambda x: x.group().replace("{{", "").replace("}}", ""), value)) for key, value in infobox.items()])
    infobox = dict([(key, re.sub(r"<.*>", "", value)) for key, value in infobox.items()])
    url = "http://ja.wikipedia.org/w/api.php?format=json&action=query&titles=Image:%s&prop=imageinfo&iiprop=url"
    response = urllib.urlopen(url % infobox[u"国旗画像"]).read()
    jres = json.loads(response)
    print jres['query']['pages']['-1']["imageinfo"][0]["url"].encode("utf-8")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default='../data/jawiki-country.json', help='input training data')
    parser.add_argument('-c', '--country', dest='country', default='イギリス', help='input training data')
    args = parser.parse_args()
    my_country = knock020.get_country_text(args.train, args.country)
    info_dic = knock025.get_info(my_country)
    main(info_dic)