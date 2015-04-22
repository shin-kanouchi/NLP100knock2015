#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/22 18:20:13 Shin Kanouchi

import argparse
from collections import defaultdict


def main(my_file):
    my_dict = defaultdict(lambda:int())
    for line in open(my_file):
        my_dict[line.strip().split()[0]] += 1

    for key, value in sorted(my_dict.items(), key=lambda x: -x[1]):
        print key, value


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    args = parser.parse_args()
    main(args.train)