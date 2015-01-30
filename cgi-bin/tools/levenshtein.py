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
    # usui-test
    # hoge = ["DABEC", "DEACB", "DAECB"]
    # hoge = ["DBECA"]
    # fuga = ["DAEBC", "BCAED", "CEAB", "EABCD", "ECDAB", "DCEAB", "EBACD", "DEBCA", "CEABD", "ADBEC"]
    # fuga = ["DAEBC", "DCEA", "ADBE", "ADBEC"]
    # fuga = ["EABCD", "ACDBE", "BDEC", "EDACB", "ADBE", "BDEAC", "DAEBC", "CDAB", "CAED", "EBACD"]

    # hoge = ["AEDCB", "BEDAC", "DBCEA", "EDACB", "EADBC"]
    # hoge = ["EAEBC"]
    # fuga = ["DECBA", "DEBCA", "DBCAE", "DCBAE", "DEBAC", "BCAE", "DCBA", "CBAE", "DBCA", "DEBA"]
    # fuga = ["CABD", "AECB", "CABE", "CABED", "BEACD", "ABED", "DEBA", "AEDCB", "BEAD", "BEAC"]

    # hoge = ["CBDAE", "CEABD", "CDBEA", "ACBDE", "ACEDB", "BDACE"]
    # hoge = ["CADBE"]
    # fuga = ["AECDB", "CEBDA", "CDBAE", "BADCE", "CEADB", "CDABE", "CBDAE", "CAEBD", "DBACE", "BDAE"]
    # fuga = ["BEDC", "DBACE", "DBAE", "CAEBD", "BADC", "AECDB", "EDCAB", "ECDB", "CDBAE", "ACDB"]

    # 2015-01-24kumiko
    # hoge = ["DEACB"]
    # fuga = ["BCAE", "DECBA", "BEACD", "DCABE", "ACBED", "DBCAE", "BEAD", "CDAB", "AEDCB", "CBADE"]
    # fuga = ["DEBC", "ADEBC", "DEBCA", "ECDBA", "DBCAE", "CAEDB", "ACDBE", "BAECD", "CEBDA", "CBDAE"]
    # hoge = ["CADBE"]
    # fuga = ["ADCEB", "BAEC", "AEBDC", "EBAD", "DCEB", "BDEC", "CEABD", "EBACD", "DECAB", "BDAEC"]
    # fuga = ["ADCEB", "CDBEA", "CEBAD", "BAECD", "CDAEB", "CEABD", "CBEAD", "CADBE", "EBACD", "BEAD"]
    # hoge = ["DBCAE"]
    # fuga = ["EDAB", "BCAE", "BCED", "BCAD", "ACDEB", "CDAB", "CEDAB", "BCAED", "DEABC", "EBADC", ]
    # fuga = ["EBADC", "DCBEA", "DCBAE", "DACBE", "DACB", "DACEB", "CADBE", "DCAEB", "BCAED", "DCBE"]
    # hoge = ["CAEDB"]
    # fuga = ["BCED", "EDAB", "ACDE", "EADC", "BCAE", "EBDC", "CEDAB", "BCAED", "ACDB", "ACDEB"]
    # fuga = ["EBADC", "CAEDB", "BCAED", "EBAD", "BADC", "CAED", "CEDAB", "EBAC", "DCBEA", "DCEBA"]

    # 2015-01-26yatsushiro
    # hoge = ["DACBE"]
    # fuga = ["DAEBC", "DEBAC", "DEBCA", "DAEB", "DEACB", "DEBC", "BEACD", "EBAC", "EBCA", "EACB"]
    # hoge = ["DEACB"]
    # fuga = ["ADCEB", "BDAC", "AEBDC", "DABCE", "ECAD", "EBAD", "ECAB", "CDAEB", "CEABD", "BAEC"]
    # hoge = ["BCADE"]
    # fuga = ["CAEDB", "EDACB", "DACBE", "DCAEB", "ACDEB", "DCEBA", "CAED", "DACB", "BCAED", "CADBE"]
    # hoge = ["DACEB"]
    # fuga = ["BAECD", "ECAB", "ACBE", "BEADC", "DACE", "EBAD", "EBACD", "DACB", "DCBE", "ECAD"]

    # 2015-01-26Osawa
    # hoge = ["DACBE"]
    # fuga = ["BADCE", "DABEC", "ECBAD", "ADCBE", "AEDB", "DAEC", "EBDAC", "DBEAC", "BDAC", "ABCDE"]
    # hoge = ["CBDAE"]
    # fuga = ["DABCE", "BAECD", "AEDCB", "EACBD", "BEDAC", "ECBAD", "BACDE", "DABC", "CEDA", "EDAC"]
    # hoge = ["DACBE"]
    # fuga = ["BCAE", "EDAB", "EADC", "BCED", "BCAD", "EBDC", "CDAB", "CEDAB", "ACDE", "ACDEB"]
    # hoge = ["DACBE"]
    # fuga = ["ECDAB", "BEDCA", "ECDA", "CDAB", "EDCA", "CDAEB", "BDAEC", "AEBDC", "DAECB", "BEDC"]

    # 2015-01-26ota
    # hoge = ["ACDBE"]
    # fuga = ["ACBED", "BACDE", "BACD", "BEACD", "ACDE", "EACDB", "ACBE", "EACD", "CBED", "EBCA"]
    # hoge = ["ACDBE"]
    # fuga = ["ACBDE", "CABDE", "CABD", "ABDE", "CBDE", "EADBC", "ACBD", "EDBCA", "EDBAC", "CEAB"]
    # hoge = ["ACDBE"]
    # fuga = ["BEDCA", "AEBDC", "CBDE", "ECDAB", "CDAEB", "EBDC", "CDAB", "ADCEB", "CABDE", "BAEC"]
    # hoge = ["DACBE"]
    # fuga = ["ADCEB", "ECDAB", "CADBE", "BDAEC", "CDAEB", "CDAB", "CADE", "CABDE", "CBDE", "AEBDC"]

    # 2015-01-26kawata
    # hoge = ["DEACB"]
    # fuga = ["CDAB", "ECDAB", "AEDCB", "BEACD", "EDAB", "BEAD", "BEAC", "DCABE", "CBADE", "ACBED"]
    # hoge = ["DACBE"]
    # fuga = ["BEDAC", "DCABE", "ACDEB", "AEBCD", "DBAE", "DBAC", "DBAEC", "EDAC", "CABE", "DABCE"]
    # hoge = ["DCAEB"]
    # fuga = ["DCBEA", "DCBAE", "EACDB", "CBEA", "DCBE", "DCBA", "EACD", "CBAE", "BEACD", "BEAC"]
    hoge = ["CADBE"]
    fuga = ["EBACD", "CDBEA", "CDBAE", "CADBE", "CADB", "CADEB", "DACBE", "CDAEB", "BDAEC", "CDBE"]

    # s1 = sys.argv[1]
    # s2 = sys.argv[2]
    for s1 in hoge:
        otaku = 0
        print s1
        for s2 in fuga:
            print s2+":", levenshtein_distance(s1, s2)
            otaku += levenshtein_distance(s1, s2)
        result = float(otaku) / len(fuga)
        print "Ave:"+str(result)

if __name__ == '__main__':
    main()
