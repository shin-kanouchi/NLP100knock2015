#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/05/27 17:41:52 Shin Kanouchi

import argparse
import knock030
from collections import Counter
import matplotlib.pyplot as plt

def main(open_file):
    word_dict = {}
    for line in open(open_file):
        w, i = line.strip().split()
        word_dict[w] = int(i)

    fig = plt.figure()# プロット領域
    ax = fig.add_subplot(111)
    ax.hist(word_dict.values(), bins=len(word_dict.values()), range=(0, 150))
    plt.title('title')
    plt.ylabel(' Type(kotonari) ')
    plt.xlabel(' Frequency ')
    ax.set_xlim(0, 150)
    ax.set_ylim(0, 100)
    plt.savefig("plt_retest49.eps")
    plt.show()


    words = [m['surface'] for sent in doc for m in sent]
    names, counts = zip(*Counter(words).most_common()[:10])

    plt.bar(range(len(names)), map(lambda x: int(x), counts), align='center')
    plt.xticks(range(len(names)), map(lambda x: x.decode('utf-8'), names))
    plt.xlim(xmin=-1)
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default='../data/knock036.txt', help='input training data')
    args = parser.parse_args()
    my_morphs = knock030.get_morphs(args.train)
    main(my_morphs)