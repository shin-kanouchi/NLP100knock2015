#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/10 23:09:49 Shin Kanouchi

import knock041


def main(all_sent):
    for a_sent in all_sent:
        for a_chunk in a_sent:
            xxWoDo = ""
            par_list = []
            sent_list = []
            for another_chunk in a_sent:
                if a_chunk.num == another_chunk.dst:
                    s1 = a_chunk.morphs_pos("動詞")
                    s2 = another_chunk.morphs_pos("名詞")
                    s3 = another_chunk.morphs_pos1("サ変接続")
                    par = another_chunk.return_morphs_par()
                    par = another_chunk.return_morphs_par()
                    if s1 and s2 and s3 and par == "を":
                        xxWoDo = "%s%s" % (another_chunk.text, a_chunk.return_Vbase())
                    elif s1 and par:
                        par_list.append(par)
                        sent_list.append(another_chunk.text)
            if xxWoDo and par_list:
                print "%s\t%s\t%s" % (xxWoDo, " ".join(par_list), " ".join(sent_list))


if __name__ == '__main__':
    all_sent = knock041.make_morph("../data/neko.cabocha")
    main(all_sent)
