#!/usr/bin/env python
# coding: UTF-8

import sys
import traceback


# エラー出力用のメソッド
def printError():
    # エラーの情報をsysモジュールから取得
    info = sys.exc_info()
    # tracebackモジュールのformat_tbメソッドで特定の書式に変換
    tbinfo = traceback.format_tb(info[2])
    print "="*60
    for tb in tbinfo:
        print tb
    print "%s" % str(info[1])
    print "="*60


# str()にしたパターンをlist()に再変換する
def convertList(pattern):
    action_list = list()
    start_word = False
    for p in pattern:
        if (p == "\'" or p == '\"') and start_word is False:
            action = str()
            start_word = True
        elif (p == "\'" or p == '\"') and start_word is True:
            action_list.append(action)
            start_word = False
        elif (p != "\'" or p != '\"') and start_word is True:
            action += p
        elif (p != "\'" or p != '\"') and start_word is False:
            pass
    return action_list


# 出力時に日本語に直す
def convertAction(pattern):
    convertedSet = list()

    for action in pattern:
        if action == "Eat":
            convertedSet.append("食事する")
        elif action == "Tea":
            convertedSet.append("お茶する")
        elif action == "Play":
            convertedSet.append("遊ぶ")
        elif action == "Sight":
            convertedSet.append("名所・名勝を見る")
        elif action == "Appreciate":
            convertedSet.append("鑑賞する")
        elif action == "Shop":
            convertedSet.append("買い物する")
    return convertedSet


# Model生成可能な形式にContext, 履歴を変換し保存
def convertUserDataForGenModel(user):
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

                    for counter in xrange(1, 41):
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
        printError()
    finally:
        if (f):
            f.close()
