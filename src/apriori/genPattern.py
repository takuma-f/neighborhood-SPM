# coding: UTF-8
import sys
import re

from itertools import chain, combinations
from optparse  import OptionParser


def getItemSetTransactionList(data_iterator):
    transaction_list = list()
    item_set         = set()
    for record in data_iterator:
        transaction = list(record)
        transaction_list.append(transaction)
        for item in transaction:
            item_set.add(frozenset([item])) # Generate 1-itemSets
    return item_set, transaction_list

def genPattern(data_iter, minSupport):
    itemSet, transaction_list = getItemSetTransactionList(data_iter)

    pattern_list = list()
    for transaction in transaction_list:
        for length in range(len(transaction)):
            pattern = list(combinations(transaction, length+1))
            for item in pattern:
                if not list(item) in pattern_list:
                    pattern_list.append(list(item))
    return transaction_list, pattern_list

def dataFromFile(fname):
    file_iter = open(fname, 'rU')
    for line in file_iter:
        line = line.strip().rstrip(',') # Remove trailing comma
        record = list(line.split(','))
        yield record

def main():
    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile', dest = 'input', help = 'the filename which contains the comma separated values', default=None)
    optparser.add_option('-s', '--minSupport', dest='minS', help = 'minimum support value', default=0.0, type='float')

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
        inFile = sys.stdin
    elif options.input is not None:
        inFile = dataFromFile(options.input)
    else:
        print 'No dataset filename specified, system with exit\n'
        sys.exit('System will exit')

    minSupport = options.minS
    transaction_list, patternList = genPattern(inFile, minSupport)

    for transaction in transaction_list:
        print "%s," % str(transaction),

    for pattern in patternList:
        print "%s," % str(pattern),

if __name__ == "__main__":
    main()