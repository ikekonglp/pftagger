import argparse
import codecs
import os
import re
import sys

parser = argparse.ArgumentParser(description='')
parser.add_argument('inputf', type=str, metavar='', help='')

A = parser.parse_args()

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

    f = codecs.open(A.inputf, "r", "utf-8")
    line_no = 0
    for line in f:
        line_no += 1
        if line_no <= 2:
            # No use, just truncate
            continue
        line = line.strip()
        args = line.split("\t")
        pos = args[0].split("/")
        print "\t".join([pos[0], pos[1], args[1]])
    f.close()
