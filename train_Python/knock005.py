#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/13 20:14:03 Shin Kanouchi

def word_ngram(my_sent, n):
    words_bi_list = []
    words = ["<s>"] + my_sent.split()
    words.append("</s>")
    for i in range( len(words) -n +1):
        words_bi_list.append(words[i:i+n])
    return words_bi_list

def char_ngram(my_sent, n):
    char_bi_list = []
    for i in range(len(my_sent) -n +1):
        if my_sent[i] == " " or my_sent[i+1] == " ": continue
        char_bi_list.append(my_sent[i:i+n])
    return char_bi_list


if __name__ == '__main__':
    my_sent = "I am an NLPer"
    print word_ngram(my_sent, 2)
    print char_ngram(my_sent, 2)