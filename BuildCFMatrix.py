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
parser.add_argument('output_dir', type=str, metavar='', help='')
parser.add_argument('pos_ori', type=int, metavar='', help='')
parser.add_argument('pos_mod', type=int, metavar='', help='')

# python BuildCFMatrix.py /media/Data/PTB/PTB_330/dev /home/lingpenk/parsing_friendly_tagger/data/ 1 2

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

    # if the original pos the same as the modified one, there is no point to generate the data anyway
    # so we just skip it
    if A.pos_ori == A.pos_mod:
        exit()

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

    # If it is "NN" replaced by the "NNS", we probably won't worry so much about it...
    # pos_o = "NN"
    # pos_n = "NNS"

    # If it is "NN" replaced by VBD, we probably will be very unhappy...

    # pos_o = "NN"
    # pos_n = "VBD"

    # read those pos tags from the command line
    pos_o = POS_DICT[A.pos_ori]
    pos_n = POS_DICT[A.pos_mod]

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


    output_ori = codecs.open(A.output_dir + "/ori_" + str(A.pos_ori) + "_" + str(A.pos_mod), "w", "utf-8")
    for sent in original_corpus:
        print_sentence(sent, output_ori)
    output_ori.close()

    output_mod = codecs.open(A.output_dir + "/mod_" + str(A.pos_ori) + "_" + str(A.pos_mod), "w", "utf-8")
    for sent in modified_corpus:
        print_sentence(sent, output_mod)
    output_mod.close()




