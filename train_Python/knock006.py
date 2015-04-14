#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/13 20:33:13 Shin Kanouchi

import knock005

my_sent1 = "paraparaparadise"
my_sent2 = "paragraph"

char_bi_list1 = knock005.char_bi(my_sent1)
char_bi_list2 = knock005.char_bi(my_sent2)
char_bi_set1 = set(char_bi_list1)
char_bi_set2 = set(char_bi_list2)

print "和集合 ->%s" % (set(char_bi_list1 + char_bi_list2))
print "積集合 ->%s" % (char_bi_set1 & char_bi_set2)
print "差集合(1)-(2) -> %s" % (char_bi_set1 - char_bi_set2)
print "差集合(2)-(1) -> %s" % (char_bi_set2 - char_bi_set1)

if "se" in char_bi_set1:
    print 'char_bi_set1 have "se"'
if "se" in char_bi_set2:
    print 'char_bi_set2 have "se"'