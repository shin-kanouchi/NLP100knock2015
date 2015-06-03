#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/03 15:09:15 Shin Kanouchi

import argparse
import knock020


def main(my_country):
    item = my_country.strip().split("\n")
    file_list = [line.strip() for line in item if line.encode("utf-8").startswith("[[ファイル:")]
    print "\n".join(file_list).encode("utf-8")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default='../data/jawiki-country.json', help='input training data')
    parser.add_argument('-c', '--country', dest='country', default='イギリス', help='input training data')
    args = parser.parse_args()
    my_country = knock020.get_country_text(args.train, args.country)
    main(my_country)