import argparse
import codecs
import os
import re
import sys
import numpy as np

parser = argparse.ArgumentParser(description='')
parser.add_argument('inputf', type=str, metavar='', help='')

A = parser.parse_args()


if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

    D = {}
    f = codecs.open(A.inputf, "r", "utf-8")
    for line in f:
        fields = line.strip().split()
        D[fields[0]] = np.array(map(float, fields[1:]))
    f.close()

    # for tag in D:
    #     print tag, D[tag]

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
    for i in xrange(1,45):
        for j in xrange(1,45):
            if i != j:
                # print POS_DICT[i]
                sys.stdout.write(POS_DICT[i] + "\t" + POS_DICT[j] + "\t")
                sys.stdout.write(str(np.linalg.norm(D[POS_DICT[i]]-D[POS_DICT[j]]))+"\n")

#end if
