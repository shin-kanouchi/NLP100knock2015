#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/13 19:54:15 Shin Kanouchi

my_sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words_len = []
words = my_sent.split()
for word in words:
    if word.endswith(',') or word.endswith('.'):
        word = word[:-1]
    words_len.append(len(word))

print words_len