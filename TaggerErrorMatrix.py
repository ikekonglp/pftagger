import argparse
import codecs
import os
import re
import sys
from collections import Counter as Counter

parser = argparse.ArgumentParser(description='')
parser.add_argument('input_gold', type=str, metavar='', help='')
parser.add_argument('input_auto', type=str, metavar='', help='')

A = parser.parse_args()


def read_corpus(filename):
    f = codecs.open(filename, "r", "utf-8")
    corpus = []
    sentence = []
    for line in f:
        if line.strip() == "":
            corpus.append(sentence)
            sentence = []
            continue
        else:
            line = line.strip()
            cline = line.split(u"\t")
            sentence.append(cline)
    f.close()
    return corpus

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

    corpus_gold = read_corpus(A.input_gold)
    corpus_auto = read_corpus(A.input_auto)

    POS_DICT = {
        1 : "NN",
        2 : "NNP",
        3 : "IN",
        4 : "DT",
        5 : "NNS",
        6 : "JJ",
        7 : ",",
        8 : "CD",
        9 : "VBD",
        10 : ".",
        11 : "RB",
        12 : "CC",
        13 : "VB",
        14 : "TO",
        15 : "VBN",
        16 : "VBZ",
        17 : "PRP",
        18 : "VBG",
        19 : "POS",
        20 : "$",
        21 : "MD",
        22 : "VBP",
        23 : "``",
        24 : "PRP$",
        25 : "'",
        26 : ":",
        27 : "WDT",
        28 : "JJR",
        29 : "RP",
        30 : "RBR",
        31 : "WRB",
        32 : "JJS",
        33 : "WP",
        34 : "-RRB-",
        35 : "-LRB-",
        36 : "EX",
        37 : "RBS",
        38 : "WP$",
        39 : "#",
        40 : "LS",
        41 : "UH",
        42 : "PDT",
        43 : "FW",
        44 : "NNPS"
    }

    POS_FIELD = 4
    
    pos_cnt = Counter()
    err_cnt = Counter()
    single_pos_err_cnt = Counter()

    for i in range(0, len(corpus_gold)):
        sent_gold = corpus_gold[i]
        sent_auto = corpus_auto[i]
        for j in range(0, len(sent_gold)):
            pos_gold = sent_gold[j][POS_FIELD]
            pos_auto = sent_auto[j][POS_FIELD]
            pos_cnt[pos_gold] += 1
            if pos_gold != pos_auto:
                # the tagger made a mistake here
                single_pos_err_cnt[pos_gold] +=1
                err_cnt[pos_gold + "\t" + pos_auto] += 1
            

    #print pos_cnt
    #print err_cnt
    sys.stdout.write("POS")
    for i in xrange(1, 45):
        sys.stdout.write("\t" + POS_DICT[i])
    sys.stdout.write("\n")


    for i in xrange(1, 45):
        sys.stdout.write(POS_DICT[i])
        for j in xrange(1, 45):
            if i == j:
                sys.stdout.write("\t0")
                continue
            else:
                err_rate_ij = 0.0
                if single_pos_err_cnt[POS_DICT[i]] > 0:
                    err_rate_ij = (float)(err_cnt[POS_DICT[i]+"\t"+POS_DICT[j]]) / (float)(single_pos_err_cnt[POS_DICT[i]])
                sys.stdout.write("\t" + str(err_rate_ij))
        err_rate_single_pos = 0.0
        if pos_cnt[POS_DICT[i]] > 0:
            err_rate_single_pos = (float)(single_pos_err_cnt[POS_DICT[i]]) / (float)(pos_cnt[POS_DICT[i]])

        sys.stdout.write("\t" + str(err_rate_single_pos) + "\t" + str(pos_cnt[POS_DICT[i]]) + "\n")



