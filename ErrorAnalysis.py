import argparse
import codecs
import os
import re
import sys

parser = argparse.ArgumentParser(description='')
parser.add_argument('inputf', type=str, metavar='', help='')
parser.add_argument('inputf2', type=str, metavar='', help='')

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

def change_line(line):
    if line[1] == u'@Username':
        line[10] = u'OOV'
        line[11] = u'OOV'
        line[12] = u'OOV'
    return line

def remove_brown(line):
    line[10] = u'OOV'
    line[11] = u'OOV'
    line[12] = u'OOV'

def remove_sel(line):
    line.pop(len(line)-1)

def change_parent(line1, line2):
    if line2[len(line2)-1] == '0':
        line1[6] = '-1'

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

    corpus = read_corpus(A.inputf)
    corpus2 = read_corpus(A.inputf2)

    for i in xrange(0, len(corpus)):
        for j in xrange(0, len(corpus[i])):
            change_parent(corpus[i][j], corpus2[i][j])

    
    # for sen in corpus:
    #   #map(lambda x: change_line(x), sen)
    #   map(lambda x: remove_brown(x), sen)
    #   #map(lambda x: remove_sel(x),sen)

    for sen in corpus:
        print_sentence(sen, sys.stdout)

#end if
