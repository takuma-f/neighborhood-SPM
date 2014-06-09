# coding: UTF-8
"""
Description    : 
Author         : 
Credits        : 

Usage:
    $python apriori.py -f DATASET.csv -s minSupport  -c minConfidence
    
    Eg.
        $ python gen_pattern.py -f sample_oku.csv -s 0.0 -c 0.0

"""

import sys
import re

from itertools     import chain, combinations
from collections import defaultdict
from optparse      import OptionParser

def subsets(arr):
    """ Returns non empty subsets of arr"""
    return chain(*[combinations(arr,i + 1) for i,a in enumerate(arr)])


def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):
    _itemSet = set()
    localSet = defaultdict(int)

    for item in itemSet:
        for transaction in transactionList:
            if item.issubset(transaction):
                freqSet[item]   += 1
                localSet[item]  += 1

    for item,count in localSet.items():
        support = float(count)/len(transactionList)
        
        if support >= minSupport:
            _itemSet.add(item)

    return _itemSet


def joinSet(itemSet,length):
    return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def getItemSetTransactionList(data_iterator):
    transactionList = list()
    itemSet         = set()
    for record in data_iterator:
        transaction = list(record)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item])) # Generate 1-itemSets
    return itemSet, transactionList


def genPattern(data_iter, minSupport):
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both: 
     - items (tuple, support)
     - rules ((pretuple, posttuple))
    """
    itemSet, transactionList = getItemSetTransactionList(data_iter)

    patternList = list()
    for transaction in transactionList:
        for length in range(len(transaction)):
            pattern = list(combinations(transaction, length+1))
            for item in pattern:
                if not list(item) in patternList:
                    patternList.append(list(item))

    return transactionList, patternList


def dataFromFile(fname):
    file_iter = open(fname, 'rU')
    for line in file_iter:
        line = line.strip().rstrip(',') # Remove trailing comma
        record = list(line.split(','))
        yield record


if __name__ == "__main__":

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
    transactionList, patternList = genPattern(inFile, minSupport)

    for transaction in transactionList:
        print "Transaction: %s" % str(transaction)

    for pattern in patternList:
        print "Pattern: %s" % str(pattern)