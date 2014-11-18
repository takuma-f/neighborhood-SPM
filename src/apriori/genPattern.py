#!/usr/bin/env python
# coding: UTF-8
import sys
import random
from itertools import combinations
from optparse import OptionParser


def getItemSetTransactionList(data_iter):
    transaction_list = list()
    item_set = set()
    for record in data_iter:
        transaction = list(record)
        transaction_list.append(transaction)
        for item in transaction:
            item_set.add(frozenset([item]))
    return item_set, transaction_list


def genPattern(data_iter, minSupport):
    itemSet, transaction_list = getItemSetTransactionList(data_iter)

    patterns = list()
    for transaction in transaction_list:
        for length in range(len(transaction)):
            pattern = list(combinations(transaction, length+1))
            for item in pattern:
                if not list(item) in patterns:
                    patterns.append(list(item))
    return transaction_list, patterns


# lengthで指定した長さのランダムパターンをquantity個持つリストを返す
def genRandomPattern(data_iter, length, quantity):
    patterns = list()
    pattern = list()

    for q in xrange(quantity):
        for l in xrange(length):
            pattern.append(random.choice(data_iter))
        patterns.append(pattern)
        pattern = list()
    return patterns


def dataFromFile(fname):
    file_iter = open(fname, 'rU')
    for line in file_iter:
        line = line.strip().rstrip(',')
        record = list(line.split(','))
        yield record


def main():
    pass

if __name__ == "__main__":
    main()
