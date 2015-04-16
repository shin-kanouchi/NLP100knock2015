#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/15 14:38:13 Shin Kanouchi

import argparse

def main(my_text):
    for line in open(my_text):
        print line.strip().replace('\t', ' ')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    args = parser.parse_args()
    main(args.train)