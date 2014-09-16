import argparse
import codecs
import os
import re
import sys

parser = argparse.ArgumentParser(description='')
parser.add_argument('inputf', type=str, metavar='', help='')

A = parser.parse_args()

# Basically, we use the Google Universal POS (v 1.03) and have them here in codes as a dictionary.
# https://code.google.com/p/universal-pos-tags/

uni_dict = {
    "!" : ".",
    "#" : ".",
    "$" : ".",
    "''" : ".",
    "(" : ".",
    ")" : ".",
    "," : ".",
    "-LRB-" : ".",
    "-RRB-" : ".",
    "." : ".",
    ":" : ".",
    "?" : ".",
    "CC" : "CONJ",
    "CD" : "NUM",
    "DT" : "DET",
    "EX" : "DET",
    "FW" : "X",
    "IN" : "ADP",
    "JJ" : "ADJ",
    "JJR" : "ADJ",
    "JJRJR" : "ADJ",
    "JJS" : "ADJ",
    "LS" : "X",
    "MD" : "VERB",
    "NN" : "NOUN",
    "NNP" : "NOUN",
    "NNPS" : "NOUN",
    "NNS" : "NOUN",
    "NP" : "NOUN",
    "PDT" : "DET",
    "POS" : "PRT",
    "PRP" : "PRON",
    "PRP$" : "PRON",
    "PRT" : "PRT",
    "RB" : "ADV",
    "RBR" : "ADV",
    "RBS" : "ADV",
    "RN" : "X",
    "RP" : "PRT",
    "SYM" : "X",
    "TO" : "PRT",
    "UH" : "X",
    "VB" : "VERB",
    "VBD" : "VERB",
    "VBG" : "VERB",
    "VBN" : "VERB",
    "VBP" : "VERB",
    "VBZ" : "VERB",
    "VP" : "VERB",
    "WDT" : "DET",
    "WH" : "X",
    "WP" : "PRON",
    "WP$" : "PRON",
    "WRB" : "ADV",
    "``" : "."
 }

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

def change_line(line):
    if line[4] in uni_dict:
        line[4] = uni_dict[line[4]]
        line[3] = line[4]
    else:
        sys.stderr.write("Tag No Match!")
        exit()


if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

    corpus = read_corpus(A.inputf)
    
    for sen in corpus:
        map(lambda x: change_line(x), sen)

    for sen in corpus:
        print_sentence(sen, sys.stdout)

#end if
