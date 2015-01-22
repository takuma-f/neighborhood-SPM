#!/usr/bin/env python
# coding: UTF-8
import sys


def levenshtein_distance(a, b):
    m = [[0] * (len(b) + 1) for i in range(len(a) + 1)]

    for i in xrange(len(a) + 1):
        m[i][0] = i

    for j in xrange(len(b) + 1):
        m[0][j] = j

    for i in xrange(1, len(a) + 1):
        for j in xrange(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                x = 0
            else:
                x = 1
            m[i][j] = min(m[i - 1][j] + 1, m[i][j - 1] + 1, m[i - 1][j - 1] + x)
    # print m
    return m[-1][-1]


def main():
    # hoge = ["D, A, B, E, C", "D, E, A, C, B", "D, A, E, C, B"]
    # fuga = ["D, A, E, B, C", "B, C, A, E, D", "C, E, A, B", "E, A, B, C, D", "E, C, D, A, B", "D, C, E, A, B", "E, B, A, C, D", "D, E, B, C, A", "C, E, A, B, D", "A, D, B, E, C"]
    # fuga = ["E, A, B, C, D", "A, C, D, B, E", "B, D, E, C", "E, D, A, C, B", "A, D, B, E", "B, D, E, A, C", "D, A, E, B, C", "C, D, A, B", "C, A, E, D", "E, B, A, C, D"]

    # hoge = ["A, E, D, C, B", "B, E, D, A, C", "D, B, C, E, A", "E, D, A, C, B", "E, A, D, B, C"]
    # fuga = ["D, E, C, B, A", "D, E, B, C, A", "D, B, C, A, E", "D, C, B, A, E", "D, E, B, A, C", "B, C, A, E", "D, C, B, A", "C, B, A, E", "D, B, C, A", "D, E, B, A"]
    # fuga = ["C, A, B, D", "A, E, C, B", "C, A, B, E", "C, A, B, E, D", "B, E, A, C, D", "A, B, E, D", "D, E, B, A", "A, E, D, C, B", "B, E, A, D", "B, E, A, C"]

    hoge = ["C, B, D, A, E", "C, E, A, B, D", "C, D, B, E, A", "A, C, B, D, E", "A, C, E, D, B", "B, D, A, C, E"]
    # fuga = ["A, E, C, D, B", "C, E, B, D, A", "C, D, B, A, E", "B, A, D, C, E", "C, E, A, D, B", "C, D, A, B, E", "C, B, D, A, E", "C, A, E, B, D", "D, B, A, C, E", "B, D, A, E"]
    fuga = ["B, E, D, C", "D, B, A, C, E", "D, B, A, E", "C, A, E, B, D", "B, A, D, C", "A, E, C, D, B", "E, D, C, A, B", "E, C, D, B", "C, D, B, A, E", "A, C, D, B"]

    # s1 = sys.argv[1]
    # s2 = sys.argv[2]
    for s1 in hoge:
        otaku = 0
        print s1
        for s2 in fuga:
            print s2, levenshtein_distance(s1, s2)
            otaku += levenshtein_distance(s1, s2)
        print otaku / len(fuga)

if __name__ == '__main__':
    main()
