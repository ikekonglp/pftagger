import argparse
import codecs
import os
import re
import sys

parser = argparse.ArgumentParser(description='')
parser.add_argument('report_dir', type=str, metavar='', help='')

A = parser.parse_args()

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

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
        25 : "\'",
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


    # sys.stdout.write("POS")
    # for i in xrange(1, 45):
    #     sys.stdout.write("\t" + POS_DICT[i])
    # sys.stdout.write("\n")
    average = 0.0
    count = 0
    weights_dict={}

    cutting_point = 25

    for i in xrange(1, 25):
        # sys.stdout.write(POS_DICT[i])
        for j in xrange(1, 45):
            if i == j:
                # sys.stdout.write(POS_DICT[i] + "\t" + POS_DICT[j] + "\t0\n")
                weights_dict[(POS_DICT[i] + "\t" + POS_DICT[j])] = 0.0
                continue
            f = codecs.open(A.report_dir + "/" + "ori_" + str(i) + "_" + str(j) + ".report", "r", "utf-8")
            acc_ori = 0
            num = 0
            for line in f:
                num +=1
                if num == 2:
                    acc_ori = line[(len(line)-8):(len(line)-2)]
                    acc_ori = float(acc_ori)
                    #print acc_ori
                    break
            f.close()

            f = codecs.open(A.report_dir + "/" + "mod_" + str(i) + "_" + str(j) + ".report", "r", "utf-8")
            acc_mod = 0
            num = 0
            for line in f:
                num +=1
                if num == 2:
                    acc_mod = line[(len(line)-8):(len(line)-2)]
                    acc_mod = float(acc_mod)
                    #print acc_mod
                    break
            f.close()

            acc_diff = acc_ori - acc_mod
            average += acc_diff
            count += 1
            # sys.stdout.write(POS_DICT[i] + "\t" + POS_DICT[j] + "\t" + str(acc_diff) + "\n")
            weights_dict[(POS_DICT[i] + "\t" + POS_DICT[j])] = acc_diff

    # sys.stdout.write("average " + str((float(average)) / ((float)(count))) )
    average = (float(average)) / ((float)(count))
    
    for i in xrange(cutting_point, 45):
        for j in xrange(1, 45):
            if i == j:
                # sys.stdout.write(POS_DICT[i] + "\t" + POS_DICT[j] + "\t0\n")
                weights_dict[(POS_DICT[i] + "\t" + POS_DICT[j])] = 0.0
                continue
            # sys.stdout.write(POS_DICT[i] + "\t" + POS_DICT[j] + "\t" + str(average) + "\n")
            weights_dict[(POS_DICT[i] + "\t" + POS_DICT[j])] = average

    # After saving all the weights to the dictionary, we now print them out together.
    # Before that, we can also do some preprocessing.

    for i in xrange(1, 45):
        for j in xrange(1, 45):
            if i == j:
                sys.stdout.write(POS_DICT[i] + "\t" + POS_DICT[j] + "\t" + str(0.0) + "\n")
                continue
            
            # sys.stdout.write(POS_DICT[i] + "\t" + POS_DICT[j] + "\t" + str(weights_dict[(POS_DICT[i] + "\t" + POS_DICT[j])]) + "\n")
            sys.stdout.write(POS_DICT[i] + "\t" + POS_DICT[j] + "\t" + str(1.0) + "\n")

    # sys.stdout.write("IDK\tIDK\t" + str(average) + "\n")
    sys.stdout.write("IDK\tIDK\t" + str(1.0) + "\n")

    