#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/13 19:50:46 Shin Kanouchi

str1 = u"パトカー"
str2 = u"タクシー"
str3 = u""

for s1, s2 in zip(str1, str2):
    str3 += s1 + s2
print str3.encode("utf-8")