import argparse
import codecs
import os
import re
import sys
from collections import Counter as Counter

parser = argparse.ArgumentParser(description='')
parser.add_argument('inputf', type=str, metavar='', help='')
#parser.add_argument('inputf2', type=str, metavar='', help='')

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

    corpus = read_corpus(A.inputf)

    # First collect all the possible POS tags
    pos_cnt = Counter()
    for sent in corpus:
        for line in sent:
            pos_cnt[line[4]] += 1

    for pos in pos_cnt:
        print str(pos) + "\t" + str(pos_cnt[pos])

    # Let's say, we want to replace the pos tag pos_o with the pos tag pos_n
    # randomly and see how many more errors we get

    # If it is "NN" replaced by the "NNS", we probably won't worry so much about it...
    pos_o = "NN"
    pos_n = "NNS"

    # If it is "NN" replaced by VBD, we probably will be very unhappy...

    pos_o = "NN"
    pos_n = "NNS"

    for sent in corpus:
        pass