#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/15 14:40:48 Shin Kanouchi

import argparse

def main(my_text):
    f1 = open('../data/col1.txt','w')
    f2 = open('../data/col2.txt','w')
    for line in open(my_text):
        itemList = line.strip().split('\t')
        item1 = itemList[0]
        item2 = itemList[1]
        f1.write(item1+"\n")
        f2.write(item2+"\n")
    f1.close()
    f2.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    args = parser.parse_args()
    main(args.train)
