#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/01 22:53:28 Shin Kanouchi
import knock041


def main(all_sent):
    for a_sent in all_sent:
        for a_chunk in a_sent:
            for another_chunk in a_sent:
                if a_chunk.num == another_chunk.dst:
                    print '%s\t%s' % (another_chunk.text, a_chunk.text)


if __name__ == '__main__':
    all_sent = knock041.make_morph("../data/neko.cabocha")
    main(all_sent)
