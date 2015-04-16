#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/15 14:29:14 Shin Kanouchi
import argparse

def main(my_text):
    return sum(1 for line in open(my_text))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    args = parser.parse_args()
    print main(args.train)
