#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
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


def main():
    # unixtime = int(time.time())
    # print unixtime
    # random.seed(unixtime)  # 乱数シードを設定(POPとrandam)
    random.seed(14213035)

    contexts = ["1", "1"]
    genre1 = "6"
    genre2 = "12"
    genre3 = "27"
    genre4 = "32"
    genre5 = "15"

    contexts = ["1", "2"]
    genre1 = "7"
    genre2 = "12"
    genre3 = "27"
    genre4 = "37"
    genre5 = "15"

    contexts = ["1", "3"]
    genre1 = "4"
    genre2 = "12"
    genre3 = "26"
    genre4 = "35"
    genre5 = "30"

    contexts = ["1", "4"]
    genre1 = "4"
    genre2 = "12"
    genre3 = "26"
    genre4 = "36"
    genre5 = "30"

    # contexts = ["2", "1"]
    # genre1 = "8"
    # genre2 = "12"
    # genre3 = "34"
    # genre4 = "25"
    # genre5 = "15"

    # contexts = ["2", "2"]
    # genre1 = "3"
    # genre2 = "12"
    # genre3 = "18"
    # genre4 = "37"
    # genre5 = "15"

    # contexts = ["2", "3"]
    # genre1 = "1"
    # genre2 = "11"
    # genre3 = "20"
    # genre4 = "30"
    # genre5 = "31"

    # contexts = ["2", "4"]
    # genre1 = "4"
    # genre2 = "12"
    # genre3 = "19"
    # genre4 = "20"
    # genre5 = "32"

    # contexts = ["3", "1"]
    # genre1 = "4"
    # genre2 = "12"
    # genre3 = "15"
    # genre4 = "25"
    # genre5 = "37"

    # contexts = ["3", "2"]
    # genre1 = "2"
    # genre2 = "12"
    # genre3 = "18"
    # genre4 = "25"
    # genre5 = "34"

    # contexts = ["3", "3"]
    # genre1 = "1"
    # genre2 = "11"
    # genre3 = "18"
    # genre4 = "14"
    # genre5 = "30"

    # contexts = ["3", "4"]
    # genre1 = "4"
    # genre2 = "12"
    # genre3 = "20"
    # genre4 = "13"
    # genre5 = "30"

    # contexts = ["4", "1"]
    # genre1 = "1"
    # genre2 = "11"
    # genre3 = "22"
    # genre4 = "23"
    # genre5 = "34"

    # contexts = ["4", "2"]
    # genre1 = "2"
    # genre2 = "11"
    # genre3 = "14"
    # genre4 = "25"
    # genre5 = "32"

    # contexts = ["4", "3"]
    # genre1 = "4"
    # genre2 = "11"
    # genre3 = "13"
    # genre4 = "15"
    # genre5 = "34"

    # contexts = ["4", "4"]
    # genre1 = "4"
    # genre2 = "12"
    # genre3 = "20"
    # genre4 = "18"
    # genre5 = "30"

    genre_set = [genre1, genre2, genre3, genre4, genre5]
    rand_p = apriori.genRandomPattern(genre_set, 5, 120)

    focus1 = "Appreciate"
    focus2 = "Shop"
    focuses = [[focus1, focus2], [focus2, focus1]]

    f1 = open("out1.txt", "a")
    f2 = open("out2.txt", "a")
    f3 = open("out3.txt", "a")
    f4 = open("out4.txt", "a")

    line1 = list()
    line2 = list()
    line3 = list()
    line4 = list()
    label1plus = 0
    label2plus = 0
    label3plus = 0
    label4plus = 0

    for x in xrange(1, 21):
        p = rand_p.pop()
        action_set = util.detParentAction(p)
        label1 = labeling(focuses, action_set, 1)
        label2 = labeling(focuses, action_set, 2)
        label3 = labeling(focuses, action_set, 3)
        label4 = labeling(focuses, action_set, 4)

        while (label1plus + label1 > 13) or (label2plus + label2 > 13) or (label3plus + label3 > 13) or (label4plus + label4 > 13):
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

if __name__ == '__main__':
    main()
