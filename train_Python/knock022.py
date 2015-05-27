#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/05/27 15:25:37 Shin Kanouchi

import argparse
import knock020
import re

category = re.compile('\[\[Category\:(((?P<cat1>.*)\|+.*)|(?P<cat2>.*))\]\]')


def main(my_country):
    item = my_country.strip().split("\n")
    for line in item:
        result = category.search(line)
        if result is not None:
            print  result.group('cat1') if result.group('cat2') is None else result.group('cat2')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default='../data/jawiki-country.json', help='input training data')
    parser.add_argument('-c', '--country', dest='country', default='イギリス', help='input training data')
    args = parser.parse_args()
    my_country = knock020.get_country_text(args.train, args.country)
    main(my_country)