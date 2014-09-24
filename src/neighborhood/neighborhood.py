#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
from itertools import combinations
from copy import deepcopy
import math

from tools import util as util


# 位置の組み合わせリストを返す
def getPositionStack(record, pattern):
    position = list()
    position_stack = list()
    position_counter = 0

    try:
        for p in pattern:
            hit = False
            for r in record:
                if p == r:
                    position.append(position_counter)
                    hit = True
                position_counter += 1  # record.index(r)は不可
            position_counter = 0
            position_stack.append(position)  # positionを統合
            position = list()
            if hit is False:
                return None  # 一つでもヒットしなければNone
        return position_stack
    except Exception:
        print "Error: getPositionStack"
        raise


# 距離の組み合わせリストを返す
def getCombinationList(record, pattern):
    combination_list = list()
    combination_counter = 0

    position_stack = getPositionStack(record, pattern)
    try:
        if position_stack is None:
            return None
        for stack in position_stack:
            if len(stack) == 1:  # positionが1個の場合
                if not combination_list:
                    for position in stack:
                        combination_list.append([position])
                    combination_counter = len(combination_list)
                else:
                    for position in stack:
                        for c in xrange(combination_counter):
                            combination_list[c].append(position)  # 既存のListにpositionを追加

            elif len(stack) > 1:  # stackにpositionが2個以上ある場合
                if not combination_list:
                    for position in stack:
                        combination_list.append([position])
                    combination_counter = len(combination_list)
                else:
                    def appendPosition(combination_list, x, combination_counter):
                        position_index = 0
                        for loop in xrange(combination_counter):
                            if loop != 0 and math.fmod(loop, len(x)) == 0:
                                position_index += 1
                            combination_list[loop].append(stack[position_index])

                    copies = deepcopy(combination_list)
                    for x in xrange(len(stack)-1):
                        for copy in copies:
                            item = deepcopy(copy)  # hack
                            combination_list.append(item)
                    combination_counter = len(combination_list)
                    appendPosition(combination_list, copies, combination_counter)
        return combination_list
    except Exception:
        print "Error: getCombinationList"
        raise


# 距離の組み合わせから矛盾したものを排除し距離を格納したリストを返す
def getDistances(record, pattern):
    distances = list()

    combination_list = getCombinationList(record, pattern)
    try:
        if combination_list is None:
            return None
        for combination in combination_list:
            diff_sum = 0  # 計算結果を初期化
            prev = 0
            first_loop = True
            for position in combination:
                if len(combination) != 1:
                    # 論理的矛盾のない前後関係のみ計算
                    if first_loop is False and prev < position:
                        diff_sum += position - prev - 1
                    elif first_loop is True:
                        diff_sum = False
                    else:
                        # 論理的矛盾でdiff_sumはFalse
                        diff_sum = False
                        break
                elif len(combination) == 1:
                    diff_sum = 0  # 要素が1個なら距離は0
                prev = position
                first_loop = False
            if diff_sum is not False:
                distances.append(diff_sum)
        if distances == []:
            return None
        else:
            return distances
    except Exception:
        print "Error: getDistances"
        raise


# 全てのトランザクションに距離を求めパターンごとに距離リストを返す
# 各パターンの出現回数も同時に返す
def getDistanceList(transaction_list, pattern):
    # あとで空のリスト生成する方法考える
    distance_list = [0, 0, 0, 0, 0, 0, 0]
    frequency_counter = 0

    try:
        for record in transaction_list:
            distances = getDistances(record, pattern)
            if distances is not None:
                for distance in distances:
                    distance_list[distance] += 1
                frequency_counter += 1
        if frequency_counter == 0:
            print "Distances:", distances
            raise Exception("Error:Failed getDistances")
        return distance_list, frequency_counter
    except Exception:
        print "Error: getDistanceList"
        raise


# パターンの距離を基に距離割合を返す
def getDistanceRate(transaction_list, pattern):
    discount = float(1) / 3  # 浮動小数点の表現のため
    index = 0
    weight = 1.0
    weight_sum = 0
    distance_list, frequency_counter = getDistanceList(transaction_list, pattern)

    # 入力した全履歴中におけるパターンの総出現回数の和を返す
    # 純粋な出現回数であり1レコード中何回出現しても出現するたび加算する
    def CountAll(distance_list):
        count = 0
        for distance in distance_list:
            count += distance
        return count
    try:
        count = CountAll(distance_list)
        for distance in distance_list:
            weight_sum += discount**index * distance * weight
            index += 1
        return weight_sum / count
    except Exception:
        print "Error: getDistanceRate"
        raise


# パターンの距離割合を基に隣接度を返す
def getNeighborhood(transaction_list, pattern):
    discount = float(1)/3  # 浮動小数点の表現のため
    neighborhood = 0

    # 入力したパターンの部分パターンをリストで返す
    # せっかくここで部分パターンの距離求めてるんだからこの値も返したい
    def getSubPattern(pattern):
        sp_list = list()
        try:
            pass
            if len(pattern) != 1:  # これでいいのか？
                sp_combinations = list(combinations(pattern, len(pattern)-1))
                for sp in sp_combinations:
                    sp_distance = getDistances(pattern, sp)
                    if sp_distance is not None:
                        sp_list.append(sp)
            return sp_list
        except Exception:
            print "Error: getSubPattern"
            raise

    sp_list = getSubPattern(pattern)
    sp_list = sorted(set(sp_list), key=sp_list.index)
    try:
        if sp_list == []:  # リストが空(=単独アイテム)なら隣接度は1
            neighborhood += 1.0
        else:
            distance_rate = getDistanceRate(transaction_list, pattern)
            for sp in sp_list:  # サブパターンの距離をgetSubPatternで返せるようにしたい
                sp_distance = getDistances(pattern, sp)
                for spd in sp_distance:
                    if len(sp) == 1:
                        neighborhood += distance_rate
                    else:
                        sp_neigh = getNeighborhood(transaction_list, sp)
                        neighborhood += discount**spd * distance_rate * sp_neigh
        return neighborhood
    except Exception:
        print "Error: getNeighborhood"
        raise


# パターンの推薦スコアを返す
def getScore(transaction_list, pattern):
    # パターンのサポート値を返す
    def getSupport(transaction_list, pattern):
        distance_list, frequency_counter = getDistanceList(transaction_list, pattern)
        return float(frequency_counter) / len(transaction_list)

    try:
        if len(pattern) == 1:
            score = 0
        else:
            score = getSupport(transaction_list, pattern) * getNeighborhood(transaction_list, pattern)
        return score
    except Exception:
        print "Error: getScore"
        raise


# confidence値によるスコアを返す
def getConfScore(transaction_list, pattern):
    # パターンのサポート値を返す
    def getSupport(transaction_list, pattern):
        distance_list, frequency_counter = getDistanceList(transaction_list, pattern)
        return float(frequency_counter) / len(transaction_list)

    try:
        if len(pattern) == 1:
            score = 0
        else:
            subpattern = deepcopy(pattern)
            del subpattern[len(pattern)-1:]
            score = getSupport(transaction_list, pattern) / getSupport(transaction_list, subpattern)
        return score
    except Exception:
        print "Error: getConfScore"
        raise


# PatternとScoreが関連づけられたdictを返す
def getDict(transaction_list, patterns):
    pattern_dict = dict()
    for pattern in patterns:
        key = str(pattern)
        pattern_dict[key] = getScore(transaction_list, pattern)
    return pattern_dict


# Patternとconfidence値によるScoreが関連づけられたdictを返す
def getConfDict(transaction_list, patterns):
    pattern_dict = dict()
    for pattern in patterns:
        key = str(pattern)
        pattern_dict[key] = getConfScore(transaction_list, pattern)
    return pattern_dict


# モジュールのテストメソッド
def test():
    # f = open("./testlog.txt", "w")
    # sys.stdout = f
    transaction_list = [["Eat", "Bar"], ["Tea", "Shop", "Eat", "Play"], ["Tea", "Shop", "Eat", "Bar"], ["Eat", "Bar"], ["Eat", "Play"], ["Play", "Bar"], ["Eat", "Bar"], ["Shop", "Eat", "Play", "Bar"]]

    patterns = [["Eat"], ["Bar"], ["Tea"], ["Shop"], ["Play"], ["Tea", "Eat"], ["Eat", "Bar"], ["Tea", "Eat", "Bar"], ["Shop", "Eat", "Play", "Bar"]]

    for pattern in patterns:
        try:
            print "Pattern:%s" % pattern
            print "Distance List:", getDistanceList(transaction_list, pattern)
            print "DistanceRate:", round(getDistanceRate(transaction_list, pattern), 3)
            print "Neighborhood:", round(getNeighborhood(transaction_list, pattern), 3)
            print "Score:", round(getConfScore(transaction_list, pattern), 3)
            print
        except Exception:
            util.printError()
    # f.close()


if __name__ == '__main__':
    test()
