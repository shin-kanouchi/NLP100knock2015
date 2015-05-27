#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/05/27 16:44:17 Shin Kanouchi

import argparse
import knock030


def main(doc):
    for sent in doc:
        for m in sent:
            if m['pos'] == '名詞' and m['pos1'] == 'サ変接続':
                print m['base']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default='../data/neko.mecab', help='input training data')
    args = parser.parse_args()
    my_morphs = knock030.get_morphs(args.train)
    main(my_morphs)