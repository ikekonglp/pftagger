import argparse
import codecs
import os
import re
import sys
from itertools import izip
from collections import Counter
import json

parser = argparse.ArgumentParser(description='')
# gold POS and gold deps
parser.add_argument('input_ref', type=str, metavar='', help='')

# gold POS but predicted deps
parser.add_argument('input_gold', type=str, metavar='', help='')

# predicted POS and prediected deps
parser.add_argument('input_sys', type=str, metavar='', help='')

# output file
parser.add_argument('outputf', type=str, metavar='', help='')

A = parser.parse_args()

POS_COL = 4
DEP_COL = 6

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

def print_sentence(sentence, outputf):
    for line in sentence:
        s = u""
        for field in line:
            s += field + u"\t"
        s = s.strip()
        outputf.write(s+u"\n")
    outputf.write(u"\n")
    return

def wrong_pos(r_sent, g_sent, s_sent):
    g_pos = [line[POS_COL] for line in g_sent]
    s_pos = [line[POS_COL] for line in s_sent]
    # print g_pos
    # print s_pos
    err_ind = [i for i in xrange(len(g_pos)) if g_pos[i]!=s_pos[i]]
    if len(err_ind) == 0:
        return None

    r_dep = [line[DEP_COL] for line in r_sent]
    g_dep = [line[DEP_COL] for line in g_sent]
    s_dep = [line[DEP_COL] for line in s_sent]

    err_num_g = len([i for i in xrange(len(r_dep)) if r_dep[i]!=g_dep[i]])
    err_num_s = len([i for i in xrange(len(r_dep)) if r_dep[i]!=s_dep[i]])
    err_num = err_num_s - err_num_g

    # print err_ind
    err_type = [str(g_pos[i]+"/"+s_pos[i]) for i in err_ind]
    cnt = Counter()
    for et in err_type:
        cnt[et] +=1
    rs = json.dumps(dict(cnt))
    return (rs, err_num)


if __name__ == '__main__':

    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

    ref_corpus = read_corpus(A.input_ref)
    gold_corpus = read_corpus(A.input_gold)
    sys_corpus = read_corpus(A.input_sys)

    output_feat = codecs.open(str(A.outputf) + ".feat", "w", "utf-8")
    output_resp = codecs.open(str(A.outputf) + ".resp", "w", "utf-8")

    ind = 0
    for r_sent, g_sent, s_sent in izip(ref_corpus, gold_corpus, sys_corpus):
        res = wrong_pos(r_sent, g_sent, s_sent)
        if res is not None:
            output_feat.write(str(ind) + "\t" + str(res[0]) + "\n")
            output_resp.write(str(ind) + "\t" + str(res[1]) + "\n")
            print res[0], res[1]
            ind +=1

    output_feat.close()
    output_resp.close()


