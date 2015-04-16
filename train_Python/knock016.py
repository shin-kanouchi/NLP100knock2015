#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/15 18:55:41 Shin Kanouchi


import argparse


def main(n, my_text, divide_name):
    my_list1 = []
    line_count = 0
    for line in open(my_text):
        my_list1.append(line.strip())
        line_count += 1

    spl_num = line_count / n

    file_count = 0
    roop_count = 0
    for line in my_list1:
        f = open('%s.%d.txt' % (divide_name, file_count), 'a')
        f.write(line+"\n")
        roop_count += 1
        if roop_count == spl_num:
            file_count += 1
            roop_count = 0
        f.close


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--N', dest='N', default=3)
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    parser.add_argument('-d', '--divide', dest='divide', default="../data/split_file", help='output divided data')

    args = parser.parse_args()
    main(int(args.N), args.train, args.divide)