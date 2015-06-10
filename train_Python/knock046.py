#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/10 19:07:21 Shin Kanouchi

import knock041


def main(all_sent):
    for a_sent in all_sent:
        for a_chunk in a_sent:
            par_list = []
            sent_list = []
            for another_chunk in a_sent:
                if a_chunk.num == another_chunk.dst:
                    V_yes = a_chunk.morphs_pos("動詞")
                    par = another_chunk.return_morphs_par()
                    if V_yes and par:
                        par_list.append(par)
                        sent_list.append(another_chunk.text)
            if par_list:
                print "%s\t%s\t%s" % (a_chunk.return_Vbase(), " ".join(par_list), " ".join(sent_list))


if __name__ == '__main__':
    all_sent = knock041.make_morph("../data/neko.cabocha")
    main(all_sent)
