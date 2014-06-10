# coding: UTF-8
"""
Date           : 2014/06/10
Description    : 
Author         : Takuma Fujitsuka(fujitsuka@uec.ac.jp)
Credits        : 

Usage:
    $python run.py -f DATASET.csv

    Eg.
        $ python run.py -f TEST_OKU.csv

"""

from apriori      import genPattern
from neighborhood import neighborhood
from optparse     import OptionParser

import sys
import re

if __name__ == '__main__':
    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile', dest = 'input', help = 'the filename which contains the comma separated values', default=None)

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
        inFile = sys.stdin
    elif options.input is not None:
        inFile = genPattern.dataFromFile(options.input)
    else:
        print 'No dataset filename specified, system with exit\n'
        sys.exit('System will exit')

    minSupport = 0.0
    transactionList, patternList = genPattern.genPattern(inFile, minSupport)
    for pattern in patternList:
        score = neighborhood.getScore(transactionList, pattern)
        print "%s Score:%s" % (pattern,score)