#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/01 22:17:52 Shin Kanouchi
"""
* 23 24D 0/1 1.373627
機関  名詞,一般,*,*,*,*,機関,キカン,キカン
に   助詞,格助詞,一般,*,*,*,に,ニ,ニ
* 24 25D 1/2 0.697440
成長  名詞,サ変接続,*,*,*,*,成長,セイチョウ,セイチョー
し   動詞,自立,*,*,サ変・スル,連用形,する,シ,シ
た   助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
EOS
"""

from collections import defaultdict


class Morph:
    def __init__(self, surf, base, pos, pos1):
        self.surf = surf
        self.base = base
        self.pos  = pos
        self.pos1 = pos1


class Chunk:
    def __init__(self, num, morphs, text, dst, srcs, head_w, head_p):
        self.num    = num
        self.morphs = morphs
        self.text   = text
        self.dst    = dst
        self.srcs   = srcs
        self.head_w = head_w
        self.head_p = head_p


    def morphs_pos(self, w):
        for morphs in self.morphs:
            if morphs.pos == w:
                return True
        return False


    def morphs_pos1(self, w):
        for morphs in self.morphs:
            if morphs.pos1 == w:
                return True
        return False


    def morphs_not_kigo(self):
        w = ""
        for morphs in self.morphs:
            if morphs.pos != "記号":
                w = w + morphs.surf
        return w


    def return_Vbase(self):
        for morphs in self.morphs:
            if morphs.pos == "動詞":
                if morphs.base != "*":
                    return morphs.base
                else:
                    return morphs.surf
        return False


    def return_morphs_par(self):
        for morphs in self.morphs:
            if morphs.pos == "助詞":
                return morphs.base
        return False


def make_morph(open_file):
    kakari_dict = defaultdict(list)
    one_sent = []
    all_sent = []
    for line in open(open_file):
        if "* " in line:
            w = line.strip().split()
            w[2] = w[2][:-1]
            one_chunk = Chunk(w[1], [], "", w[2], [], "", "")
            kakari_dict[w[2]].append(w[1])
            one_sent.append(one_chunk)
            i = 0
        elif "\t" in line:
            surf, item = line.strip().split("\t")
            items = item.split(",")
            one_chunk.morphs.append(Morph(surf, items[6], items[0], items[1]))
            if items[0] != "記号":
                one_chunk.text = one_chunk.text + surf
            if i == int(w[3][0]):
                if items[6]== "*":
                    items[6] = surf
                one_chunk.head_w = items[6]
                one_chunk.head_p = items[0]
            i += 1
        elif "EOS" in line:
            for one_chunk in one_sent:
                one_chunk.srcs = kakari_dict[one_chunk.num]
            all_sent.append(one_sent)
            one_sent = []
            kakari_dict = defaultdict(list)
    return all_sent


if __name__ == '__main__':
    all_sent = make_morph("../data/neko.cabocha")
    for a_chunk in all_sent[8]:
        print 'num=%s\tdst=%s\tsrcs=%s' % (a_chunk.num, a_chunk.dst, a_chunk.srcs)
        for m in a_chunk.morphs:
            print 'surface=%s\tbase=%s\tpos=%s' % (m.surf, m.base, m.pos)
