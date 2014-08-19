import argparse
import codecs
import os
import re
import sys
from collections import Counter as Counter
import random
import copy

parser = argparse.ArgumentParser(description='')
parser.add_argument('inputf', type=str, metavar='', help='')
parser.add_argument('output_ori', type=str, metavar='', help='')
parser.add_argument('output_mod', type=str, metavar='', help='')

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

def print_sentence(sentence, outputf):
    for line in sentence:
        s = u""
        for field in line:
            s += field + u"\t"
        s = s.strip()
        outputf.write(s+u"\n")
    outputf.write(u"\n")
    return

def convert_line(cl):
    tag = cl[4]
    cl[3] = tag
    if tag == "PRP" or tag == "PRP$":
        pass
    elif len(tag) > 2:
        cl[3] = tag[:2]
    return cl

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

    corpus = read_corpus(A.inputf)

    POS_FIELD = 4

    # First collect all the possible POS tags
    # pos_cnt = Counter()
    # for sent in corpus:
    #     for line in sent:
    #         pos_cnt[line[POS_FIELD]] += 1

    # for pos in pos_cnt:
    #     print str(pos) + "\t" + str(pos_cnt[pos])

    # Let's say, we want to replace the pos tag pos_o with the pos tag pos_n
    # randomly and see how many more errors we get



    # If it is "NN" replaced by the "NNS", we probably won't worry so much about it...
    # pos_o = "NN"
    # pos_n = "NNS"

    # If it is "NN" replaced by VBD, we probably will be very unhappy...

    pos_o = "NN"
    pos_n = "VBD"

    original_corpus = []
    modified_corpus = []
    for sent in corpus:
        pos_o_index_list = []
        for i in range(0,len(sent)):
            if sent[i][POS_FIELD] == pos_o:
                pos_o_index_list.append(i)
        if len(pos_o_index_list) > 0:
            o_sent = copy.deepcopy(sent)
            original_corpus.append(o_sent)
            # Random select a word with the pos pos_o
            r_index = random.choice(pos_o_index_list)
            # Change it to the new POS
            sent[r_index][POS_FIELD] = pos_n
            map(lambda x : convert_line(x), sent)
            # else this sentence does not contain pos_o, should be skipped
            modified_corpus.append(sent)


    output_ori = codecs.open(A.output_ori, "w", "utf-8")
    for sent in original_corpus:
        print_sentence(sent, output_ori)
    output_ori.close()

    output_mod = codecs.open(A.output_mod, "w", "utf-8")
    for sent in modified_corpus:
        print_sentence(sent, output_mod)
    output_mod.close()




