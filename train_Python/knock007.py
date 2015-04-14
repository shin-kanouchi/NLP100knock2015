#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/14 10:52:30 Shin Kanouchi


def main(x, y, z):
    my_text = "%s時の%sは%s" % (x, y, z)
    return my_text

if __name__ == '__main__':
    x = 12
    y = "気温"
    z = 22.4
    print main(x, y, z)