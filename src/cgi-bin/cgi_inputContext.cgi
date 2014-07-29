#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
import cgi
from apriori import genPattern as apriori
from apriori import genIter as genIter
from model import model as svm
from tools import util as util


def convertUserDataForGenModel(user):
    # Model生成可能な形式にContext, 履歴を変換し保存
    f = None
    model_f = None
    result = ""
    try:
        f = open('userData/'+user+'_history.txt', 'r')
        for line in f:
            splited_line = line.split(', ')
            splited_line
            rates = splited_line[18:23]
            companion = splited_line[1]
            budget = splited_line[2]
            genres = splited_line[8:13]
            for (rate, genre) in zip(rates, genres):
                if int(genre) != 0:
                    result += str(rate).replace(('\r\n'or'\r'or'\n'), '')
                    for counter in xrange(0, 4):
                        if counter == int(companion):
                            result += " "+str(counter+1)+":1"
                        else:
                            result += " "+str(counter+1)+":0"

                    for counter in xrange(0, 5):
                        if counter == int(budget):
                            result += " "+str(counter+5)+":1"
                        else:
                            result += " "+str(counter+5)+":0"

                    for counter in xrange(1, 32):
                        if counter == int(genre):
                            result += " "+str(counter+9)+":1"
                        else:
                            result += " "+str(counter+9)+":0"
                    result += "\r\n"
                else:
                    pass
        model_f = open('userData/'+user+'_svm.txt', 'w')
        model_f.write(result)
    except IOError:
        util.printError()
    finally:
        if (f):
            f.close()


def main():
    print "<!DOCTYPE html>"
    print
    print """
    <html lang="ja">
    <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="素晴らしくNice choice.な">
    <meta name="TakumaFUJITSUKA" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Perfect Planner</title>
    </head>

    <body>
    """

    input_data = cgi.FieldStorage()
    user = input_data["userId"].value

    # ユーザーのモデルを生成
    convertUserDataForGenModel(user)
    model = svm.genModel(user)
    svm.saveModel(user+'.model', model)

    data_iter = genIter.getDataIter(user, model, input_data)
    minSupport = 0.0
    transaction_list, pattens = apriori.genPattern(data_iter, minSupport)
    print transaction_list

    print "</body></html>"
    import cgitb
    cgitb.enable()


if __name__ == '__main__':
    main()
