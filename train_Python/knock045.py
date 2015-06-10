#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/10 18:39:23 Shin Kanouchi

import knock041
from collections import defaultdict


def main(all_sent):
    V_dict = defaultdict(list)
    for a_sent in all_sent:
        for a_chunk in a_sent:
            for another_chunk in a_sent:
                if a_chunk.num == another_chunk.dst:
                    s1 = a_chunk.morphs_pos("動詞")
                    s2 = another_chunk.morphs_pos("名詞")
                    Ver = a_chunk.return_morphs_base()
                    Par = another_chunk.return_morphs_par()
                    if s1 and s2 and Par:
                        V_dict[Ver].append(Par)
                        #print '%s\t%s' % (Ver, Par)
    return V_dict


def print_dict(V_dict):
    for k, Par_list in V_dict.items():
        print k, " ".join(set(Par_list))


if __name__ == '__main__':
    all_sent = knock041.make_morph("../data/neko.cabocha")
    V_dict = main(all_sent)
    print_dict(V_dict)