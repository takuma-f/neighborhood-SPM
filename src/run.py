# coding: UTF-8
from apriori      import gen_pattern
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
        inFile = gen_pattern.dataFromFile(options.input)
    else:
        print 'No dataset filename specified, system with exit\n'
        sys.exit('System will exit')

    minSupport    = 0.0
    transactionList, patternList = genPattern.genPattern(inFile, minSupport)
    for pattern in patternList:
        score = neighborhood.getScore(transactionList, pattern)
        print "Pattern:%s Score:%s" % (pattern,score)