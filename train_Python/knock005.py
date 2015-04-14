#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/13 20:14:03 Shin Kanouchi

def word_bi(my_sent):
    words_bi_list = []
    words = ["<s>"] + my_sent.split()
    words.append("</s>")
    for i in range(len(words)-1):
        words_bi_list.append("%s %s" % (words[i], words[i+1]))
    return words_bi_list

def char_bi(my_sent):
    char_bi_list = []
    for i in range(len(my_sent)-1):
        #if my_sent[i] == " " or my_sent[i+1] == " ": continue
        char_bi_list.append("%s%s" % (my_sent[i], my_sent[i+1]))
    return char_bi_list


if __name__ == '__main__':
    my_sent = "I am an NLPer"
    print word_bi(my_sent)
    print char_bi(my_sent)
