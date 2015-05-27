#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/05/27 17:30:47 Shin Kanouchi

import argparse
import knock030
from collections import Counter

def main(doc):
    words = [m['surface'] for sent in doc for m in sent]
    for word, count in Counter(words).most_common():
        print count, word

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default='../data/neko.mecab', help='input training data')
    args = parser.parse_args()
    my_morphs = knock030.get_morphs(args.train)
    main(my_morphs)