#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/05/27 16:45:31 Shin Kanouchi

import argparse
import knock030


def main(doc):
    for sent in doc:
        for i in range(1, len(sent) - 1):
            if sent[i-1]['pos'] == '名詞' and sent[i]['surface'] == 'の' and sent[i+1]['pos'] == '名詞':
                print sent[i-1]['surface'], sent[i]['surface'], sent[i+1]['surface']


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default='../data/neko.mecab', help='input training data')
    args = parser.parse_args()
    my_morphs = knock030.get_morphs(args.train)
    main(my_morphs)