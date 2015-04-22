#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/22 18:15:26 Shin Kanouchi

import argparse


def main(train_file):
    items = []
    for line in open(train_file):
        items.append(line.strip().split('\t'))

    for spl in sorted(items, key=lambda x: -float(x[2])):
        print ' '.join(spl)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    args = parser.parse_args()
    main(args.train)