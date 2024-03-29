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
# JSON扱えるようになればもっとマシなコードにできるはず...
def convertAction(pattern):
    convertedSet = list()

    for action in pattern:
        if action == "1":
            convertedSet.append("和食・寿司")
        elif action == "2":
            convertedSet.append("中華料理")
        elif action == "3":
            convertedSet.append("焼肉・焼き物・韓国料理")
        elif action == "4":
            convertedSet.append("イタリアン・フレンチ他洋食")
        elif action == "5":
            convertedSet.append("ファミリーレストラン")
        elif action == "6":
            convertedSet.append("定食")
        elif action == "7":
            convertedSet.append("カレー・アジア料理")
        elif action == "8":
            convertedSet.append("ラーメン・麺類")
        elif action == "9":
            convertedSet.append("ファストフード・牛丼")
        elif action == "10":
            convertedSet.append("居酒屋・バー")
        elif action == "11":
            convertedSet.append("カフェ・スイーツ（和風）")
        elif action == "12":
            convertedSet.append("カフェ・スイーツ（洋風）")
        elif action == "13":
            convertedSet.append("遊園地")
        elif action == "14":
            convertedSet.append("水族館")
        elif action == "15":
            convertedSet.append("映画館・劇場")
        elif action == "16":
            convertedSet.append("カラオケ・ゲームセンター")
        elif action == "17":
            convertedSet.append("スポーツ施設")
        elif action == "18":
            convertedSet.append("レジャー施設")
        elif action == "19":
            convertedSet.append("イベント会場")
        elif action == "20":
            convertedSet.append("温泉・リゾート施設")
        elif action == "21":
            convertedSet.append("夜遊び・ディスコクラブ")
        elif action == "22":
            convertedSet.append("神社・仏閣")
        elif action == "23":
            convertedSet.append("史跡")
        elif action == "24":
            convertedSet.append("展望台・タワー")
        elif action == "25":
            convertedSet.append("公園・庭園")
        elif action == "26":
            convertedSet.append("博物館")
        elif action == "27":
            convertedSet.append("美術館・ギャラリー")
        elif action == "28":
            convertedSet.append("資料館・ミュージアム")
        elif action == "29":
            convertedSet.append("百貨店")
        elif action == "30":
            convertedSet.append("ファッション")
        elif action == "31":
            convertedSet.append("食品（持ち帰り）")
        elif action == "32":
            convertedSet.append("菓子（持ち帰り）")
        elif action == "33":
            convertedSet.append("酒類（持ち帰り）")
        elif action == "34":
            convertedSet.append("雑貨・土産物")
        elif action == "35":
            convertedSet.append("食器・花器")
        elif action == "36":
            convertedSet.append("宝飾品")
        elif action == "37":
            convertedSet.append("書店")
        elif action == "38":
            convertedSet.append("家電量販店")
        elif action == "39":
            convertedSet.append("スポーツ用品店")
        elif action == "40":
            convertedSet.append("家具屋")
        elif action == "41":
            convertedSet.append("その他趣味品")
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

if __name__ == '__main__':
    convertUserDataForGenModel("0140004")
