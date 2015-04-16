#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/15 14:46:47 Shin Kanouchi

import argparse
import sys


def main(col1, col2):
    my_list1 = []
    my_list2 = []
    for line1 in open(col1):
        my_list1.append(line1.strip()) 

    for line2 in open(col2):
        my_list2.append(line2.strip())

    if len(my_list1) != len(my_list2):
        print >> sys.stderr, "Total lines are not same."
    else:
        for i in range(len(my_list1)):
            print my_list1[i] + "\t" + my_list2[i]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--col1', dest='col1', default="../data/col1.txt")
    parser.add_argument('-o', '--col2', dest='col2', default="../data/col1.txt")
    args = parser.parse_args()
    main(args.col1, args.col2)