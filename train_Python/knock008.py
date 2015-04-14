#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/14 10:56:11 Shin Kanouchi
import sys

def cipher(my_text):
    new_text = ""
    for char in my_text:
        if char.islower():
            char = chr(219 - ord(char))
        new_text += char
    return new_text


if __name__ == '__main__':
    my_text = sys.stdin.readline()#"acBBBa"
    print cipher(my_text)