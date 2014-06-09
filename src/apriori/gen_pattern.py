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
    """calculates the support for items in the itemSet and returns a subset of the itemSet 
    each of whose elements satisfies the minimum support"""
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
    """Join a set with itself and returns the n-element itemsets"""
    return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])

def getItemSetTransactionList(data_iterator):
    transactionList = list() # 履歴の集合を格納する
    itemSet         = set() # 行動の集合を格納する
    for record in data_iterator:
        transaction = frozenset(record)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item])) # Generate 1-itemSets
    return itemSet, transactionList

def runApriori(data_iter, minSupport, minConfidence):
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both: 
     - items (tuple, support)
     - rules ((pretuple, posttuple), confidence)
    """
    itemSet, transactionList = getItemSetTransactionList(data_iter)

    freqSet     = defaultdict(int)
    largeSet    = dict() # Global dictionary which stores (key=n-itemSets,value=support) which satisfy minSupport
    assocRules  = dict() # Dictionary which stores Association Rules

    oneCSet     = returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet)
    
    currentLSet = oneCSet
    k = 2
    while(currentLSet != set([])):
        largeSet[k-1]   = currentLSet
        currentLSet     = joinSet(currentLSet,k)
        currentCSet     = returnItemsWithMinSupport(currentLSet, transactionList, minSupport, freqSet)
        currentLSet     = currentCSet
        k = k + 1

    patternList=list()
    for key,value in largeSet.items():
        patternList.extend(list(item) for item in value)

    return transactionList, patternList

def dataFromFile(fname):
    """Function which reads from the file and yields a generator"""
    file_iter = open(fname, 'rU')
    for line in file_iter:
        line = line.strip().rstrip(',') # Remove trailing comma
        record = frozenset(line.split(','))
        yield record

def printResults(items):
    """prints the generated itemsets and the confidence rules"""
    for pattern in items:
        print "Pattern : %s" % str(pattern)

if __name__ == "__main__":

    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile', dest = 'input', help = 'the filename which contains the comma separated values', default=None)
    optparser.add_option('-s', '--minSupport', dest='minS', help = 'minimum support value', default=0.15, type='float')
    optparser.add_option('-c','--minConfidence', dest='minC', help = 'minimum confidence value', default = 0.6, type='float')

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
        inFile = sys.stdin
    elif options.input is not None:
        inFile = dataFromFile(options.input)
    else:
        print 'No dataset filename specified, system with exit\n'
        sys.exit('System will exit')

    minSupport    = options.minS
    minConfidence = options.minC
    items  = runApriori(inFile, minSupport, minConfidence)

    printResults(items)
