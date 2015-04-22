#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/15 18:55:41 Shin Kanouchi

import argparse


def main(n, my_text, divide_name):
    my_list1 = []
    for line in open(my_text):
        my_list1.append(line.strip())

    l = len(my_list1) / n
    all_list = [my_list1[x:x + l] for x in xrange(0, len(my_list1), l)]
    for i in range(n):
        f = open('%s.%d.txt' % (divide_name, i), 'w')
        f.write("\n".join(all_list[i - 1]))
        f.close


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--N', dest='N', default=3)
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    parser.add_argument('-d', '--divide', dest='divide', default="../data/split_file", help='output divided data')

    args = parser.parse_args()
    main(int(args.N), args.train, args.divide)