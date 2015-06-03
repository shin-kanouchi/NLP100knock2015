#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/03 17:19:57 Shin Kanouchi

import argparse
import knock020


def get_info(my_country):
    item = my_country.strip().split("\n}}\n")[0].split("\n")
    infobox = [line.strip() for line in item if line.encode("utf-8").startswith("|")]
    return dict([tuple(line.split("<ref>")[0].replace("|", "").split(" = ")) for line in infobox])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default='../data/jawiki-country.json', help='input training data')
    parser.add_argument('-c', '--country', dest='country', default='イギリス', help='input training data')
    args = parser.parse_args()
    my_country = knock020.get_country_text(args.train, args.country)
    info_dic = get_info(my_country)
    print "\n".join([key+": "+info_dic[key] for key in info_dic.keys()])