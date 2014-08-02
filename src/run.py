#!/usr/bin/env python
# coding: UTF-8
"""
Date        : 2014/06/10
Description :
Author      : Takuma Fujitsuka(fujitsuka@uec.ac.jp)
Credits     :

Usage:
    $python run.py -f DATASET.csv

    Eg.
        $ python run.py -f TEST.csv

"""

from apriori import genPattern as apriori
from neighborhood import neighborhood as neigh
from optparse import OptionParser  # optparseは非推奨
import sys


def main():
    # 単体実行時はCSVを引数に実行
    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile', dest='input', default=None)

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
        inFile = sys.stdin
    elif options.input is not None:
        inFile = apriori.dataFromFile(options.input)
    else:
        print 'No dataset filename specified, system with exit\n'
        sys.exit('System will exit')

    minSupport = 0.0
    transaction_list, pattern_list = apriori.genPattern(inFile, minSupport)
    for pattern in pattern_list:
        score = neigh.getScore(transaction_list, pattern)
        print "%s Score:%s" % (pattern, score)


if __name__ == '__main__':
    main()
