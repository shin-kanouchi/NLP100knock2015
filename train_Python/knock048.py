#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/10 23:48:45 Shin Kanouchi

import knock041


def main(all_sent):
    for sent in all_sent:
        for chunk in sent:
            dst_int = int(chunk.dst)
            if int(chunk.dst) != -1 and chunk.morphs_pos("名詞"):
                outputs = chunk.text
                while dst_int != -1:
                    outputs += ' -> %s' % sent[dst_int].text
                    dst_int = int(sent[dst_int].dst)
                print '%s' % outputs


if __name__ == '__main__':
    all_sent = knock041.make_morph("../data/neko.cabocha")
    main(all_sent)
