#!/usr/bin/env python
# coding: UTF-8

# 実験用のテストデータを出力するスクリプトです
# 実行すると二つの行動の距離の関係性に着目した4種類のファイルを出力します
# 現在は一回の実行で各出力ファイルに正負20個づつのテストデータを吐きます

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/cgi-bin/')
sys.stderr = sys.stdout
import random
import time

from apriori import genPattern as apriori
from neighborhood import neighborhood as neigh
from tools import util as util


def labeling(focuses, p, mode):
    counter = 1
    for f in focuses:
        dist = neigh.getDistances(p, f)
        if mode == 1:
            if (dist is not None) and (dist[0] < 2):
                return 1
            elif (dist is not None) and (dist[0] >= 2):
                return -1
            else:
                pass
        elif mode == 2:
            if counter == 1:
                if (dist is not None) and (dist[0] < 2):
                    return -1
                elif (dist is not None) and (dist[0] >= 2):
                    return 1
                else:
                    pass
            elif counter == 2:
                if (dist is not None) and (dist[0] < 2):
                    return 1
                elif (dist is not None) and (dist[0] >= 2):
                    return -1
                else:
                    pass
            counter += 1
        elif mode == 3:
            if counter == 1:
                if (dist is not None) and (dist[0] < 2):
                    return 1
                elif (dist is not None) and (dist[0] >= 2):
                    return -1
                else:
                    pass
            elif counter == 2:
                if (dist is not None) and (dist[0] < 2):
                    return -1
                elif (dist is not None) and (dist[0] >= 2):
                    return 1
                else:
                    pass
            counter += 1
        elif mode == 4:
            if (dist is not None) and (dist[0] < 2):
                return -1
            elif (dist is not None) and (dist[0] >= 2):
                return 1
            else:
                pass


def genLine(contexts, actions, genres, label):
    line = str()
    line += ("1900-01-01, ")
    for c in contexts:
        line += str(c) + ", "
    for a in actions:
        line += str(a) + ", "
    for g in genres:
        line += str(g) + ", "
    for a in actions:
        line += str(a) + ", "
    line += str(label)
    return line


def genData(contexts, genre1, genre2, genre3, genre4, genre5, focus1 = "Eat", focus2 = "Play"):
    # unixtime = int(time.time())
    # print unixtime
    # random.seed(unixtime)  # 乱数シードを設定(POPとrandam)
    random.seed(14213035)

    if focus1 == "Eat" and focus2 == "Tea":
        f1 = open("001_history.txt", "a")
        f2 = open("002_history.txt", "a")
        f3 = open("003_history.txt", "a")
        f4 = open("004_history.txt", "a")
    elif focus1 == "Eat" and focus2 == "Play":
        f1 = open("005_history.txt", "a")
        f2 = open("006_history.txt", "a")
        f3 = open("007_history.txt", "a")
        f4 = open("008_history.txt", "a")
    elif focus1 == "Eat" and focus2 == "Sight":
        f1 = open("009_history.txt", "a")
        f2 = open("010_history.txt", "a")
        f3 = open("011_history.txt", "a")
        f4 = open("012_history.txt", "a")
    elif focus1 == "Eat" and focus2 == "Appreciate":
        f1 = open("013_history.txt", "a")
        f2 = open("014_history.txt", "a")
        f3 = open("015_history.txt", "a")
        f4 = open("016_history.txt", "a")
    elif focus1 == "Eat" and focus2 == "Shop":
        f1 = open("017_history.txt", "a")
        f2 = open("018_history.txt", "a")
        f3 = open("019_history.txt", "a")
        f4 = open("020_history.txt", "a")
    elif focus1 == "Tea" and focus2 == "Play":
        f1 = open("021_history.txt", "a")
        f2 = open("022_history.txt", "a")
        f3 = open("023_history.txt", "a")
        f4 = open("024_history.txt", "a")
    elif focus1 == "Tea" and focus2 == "Sight":
        f1 = open("025_history.txt", "a")
        f2 = open("026_history.txt", "a")
        f3 = open("027_history.txt", "a")
        f4 = open("028_history.txt", "a")
    elif focus1 == "Tea" and focus2 == "Appreciate":
        f1 = open("029_history.txt", "a")
        f2 = open("030_history.txt", "a")
        f3 = open("031_history.txt", "a")
        f4 = open("032_history.txt", "a")
    elif focus1 == "Tea" and focus2 == "Shop":
        f1 = open("033_history.txt", "a")
        f2 = open("034_history.txt", "a")
        f3 = open("035_history.txt", "a")
        f4 = open("036_history.txt", "a")
    elif focus1 == "Play" and focus2 == "Sight":
        f1 = open("037_history.txt", "a")
        f2 = open("038_history.txt", "a")
        f3 = open("039_history.txt", "a")
        f4 = open("040_history.txt", "a")
    elif focus1 == "Play" and focus2 == "Appreciate":
        f1 = open("041_history.txt", "a")
        f2 = open("042_history.txt", "a")
        f3 = open("043_history.txt", "a")
        f4 = open("044_history.txt", "a")
    elif focus1 == "Play" and focus2 == "Shop":
        f1 = open("045_history.txt", "a")
        f2 = open("046_history.txt", "a")
        f3 = open("047_history.txt", "a")
        f4 = open("048_history.txt", "a")
    elif focus1 == "Sight" and focus2 == "Shop":
        f1 = open("049_history.txt", "a")
        f2 = open("050_history.txt", "a")
        f3 = open("051_history.txt", "a")
        f4 = open("052_history.txt", "a")
    elif focus1 == "Appreciate" and focus2 == "Shop":
        f1 = open("053_history.txt", "a")
        f2 = open("054_history.txt", "a")
        f3 = open("055_history.txt", "a")
        f4 = open("056_history.txt", "a")

    genre_set = [genre1, genre2, genre3, genre4, genre5]
    rand_p = apriori.genRandomPattern(genre_set, 5, 120)

    # Eat Tea Play Sight Appreciate Shop

    focuses = [[focus1, focus2], [focus2, focus1]]
    line1 = list()
    line2 = list()
    line3 = list()
    line4 = list()
    label1plus = 0
    label2plus = 0
    label3plus = 0
    label4plus = 0

    for x in xrange(1, 31):
        p = rand_p.pop()
        action_set = util.detParentAction(p)
        label1 = labeling(focuses, action_set, 1)
        label2 = labeling(focuses, action_set, 2)
        label3 = labeling(focuses, action_set, 3)
        label4 = labeling(focuses, action_set, 4)
        while (label1plus + label1 > 20) or (label2plus + label2 > 20) or (label3plus + label3 > 20) or (label4plus + label4 > 20):  # Empty listエラーが出る時はこちらを使う
            p = rand_p.pop()
            action_set = util.detParentAction(p)
            label1 = labeling(focuses, action_set, 1)
            label2 = labeling(focuses, action_set, 2)
            label3 = labeling(focuses, action_set, 3)
            label4 = labeling(focuses, action_set, 4)

        if label1 == 1:
            label1plus += 1
            # print "label1:"+str(label1plus)
        if label2 == 1:
            label2plus += 1
            # print "label2:"+str(label2plus)
        if label3 == 1:
            label3plus += 1
            # print "label3:"+str(label3plus)
        if label4 == 1:
            label4plus += 1
            # print "label4:"+str(label4plus)

        line1.append(genLine(contexts, action_set, p, label1))
        line2.append(genLine(contexts, action_set, p, label2))
        line3.append(genLine(contexts, action_set, p, label3))
        line4.append(genLine(contexts, action_set, p, label4))
    for line in line1:
        f1.write(str(line) + "\r\n")
    for line in line2:
        f2.write(str(line) + "\r\n")
    for line in line3:
        f3.write(str(line) + "\r\n")
    for line in line4:
        f4.write(str(line) + "\r\n")
    if(f1 or f2 or f3 or f4):
        f1.close()
        f2.close()
        f3.close()
        f4.close()


def main():
    contexts = ["1", "1"]
    genre1 = "6"
    genre2 = "12"
    genre3 = "27"
    genre4 = "32"
    genre5 = "15"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

    contexts = ["1", "2"]
    genre1 = "7"
    genre2 = "12"
    genre3 = "27"
    genre4 = "37"
    genre5 = "15"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

    # contexts = ["1", "3"]
    # genre1 = "4"
    # genre2 = "12"
    # genre3 = "26"
    # genre4 = "35"
    # genre5 = "30"
    # genData(contexts, genre1, genre2, genre3, genre4, genre5)

    # contexts = ["1", "4"]
    # genre1 = "4"
    # genre2 = "12"
    # genre3 = "26"
    # genre4 = "36"
    # genre5 = "30"
    # genData(contexts, genre1, genre2, genre3, genre4, genre5)

    contexts = ["2", "1"]
    genre1 = "8"
    genre2 = "12"
    genre3 = "34"
    genre4 = "25"
    genre5 = "15"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

    contexts = ["2", "2"]
    genre1 = "3"
    genre2 = "12"
    genre3 = "18"
    genre4 = "37"
    genre5 = "15"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

    contexts = ["2", "3"]
    genre1 = "1"
    genre2 = "11"
    genre3 = "20"
    genre4 = "30"
    genre5 = "31"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

    contexts = ["2", "4"]
    genre1 = "4"
    genre2 = "12"
    genre3 = "19"
    genre4 = "20"
    genre5 = "32"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

    contexts = ["3", "1"]
    genre1 = "4"
    genre2 = "12"
    genre3 = "15"
    genre4 = "25"
    genre5 = "37"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

    contexts = ["3", "2"]
    genre1 = "2"
    genre2 = "12"
    genre3 = "18"
    genre4 = "25"
    genre5 = "34"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

    contexts = ["3", "3"]
    genre1 = "1"
    genre2 = "11"
    genre3 = "18"
    genre4 = "14"
    genre5 = "30"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

    contexts = ["3", "4"]
    genre1 = "4"
    genre2 = "12"
    genre3 = "20"
    genre4 = "13"
    genre5 = "30"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

    # contexts = ["4", "1"]
    # genre1 = "1"
    # genre2 = "11"
    # genre3 = "22"
    # genre4 = "23"
    # genre5 = "34"
    # genData(contexts, genre1, genre2, genre3, genre4, genre5)

    contexts = ["4", "2"]
    genre1 = "2"
    genre2 = "11"
    genre3 = "14"
    genre4 = "25"
    genre5 = "32"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

    contexts = ["4", "3"]
    genre1 = "4"
    genre2 = "11"
    genre3 = "13"
    genre4 = "15"
    genre5 = "34"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

    contexts = ["4", "4"]
    genre1 = "4"
    genre2 = "12"
    genre3 = "20"
    genre4 = "18"
    genre5 = "30"
    genData(contexts, genre1, genre2, genre3, genre4, genre5)

if __name__ == '__main__':
    main()