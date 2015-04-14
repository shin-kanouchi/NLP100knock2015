#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/13 20:02:22 Shin Kanouchi

my_sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
my_dict = {}
head = [1, 5, 6, 7, 8, 9, 15, 16, 19]
words = my_sent.split()
for i in range(len(words)):
    if i+1 in head:
        j=1
    else:
        j=2
    my_dict[words[i][:j]] = i+1

for k, v in sorted(my_dict.items(), key=lambda x:x[1]):
        print k, v