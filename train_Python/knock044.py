#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/01 23:24:53 Shin Kanouchi


def main(NP_VP_line):
    print "digraph knock60{"
    for line in open(NP_VP_line):
        line = line.replace('\"',r'\"')
        item = line.strip().split('\t')
        print '\t"%s" -> "%s";' % (item[0],item[1])
    print "}"

if __name__ == '__main__':
    main("../data/knock043.txt")