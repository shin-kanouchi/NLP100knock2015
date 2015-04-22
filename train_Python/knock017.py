#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/22 17:50:29 Shin Kanouchi

import argparse


def main(train_file):
    my_dict = dict()
    for line in open(train_file):
        my_dict[line.strip().split("\t")[0]] = 0

    for key in my_dict.keys():
        print key


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    args = parser.parse_args()
    main(args.train)