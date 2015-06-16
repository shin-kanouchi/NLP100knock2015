#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/15 19:52:30 Shin Kanouchi

import re
re_sent = re.compile(r"(\.|\;|\:|\?|\!) ([A-Z])")


def main(in_fname):
    for line in open(in_fname):
        print '\n'.join(line.split(' '))

if __name__ == '__main__':
    main("../data/knock050.txt")
