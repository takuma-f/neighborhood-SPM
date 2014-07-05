# coding: UTF-8
from itertools import combinations
from copy import deepcopy
import math

def getCombinationList(record, pattern):
    # 距離の組み合わせリストを返す
    distance            = list()
    position            = list()
    position_stack      = list()
    combination_list    = list()
    position_counter    = 0
    combination_counter = 0

    for p in pattern:    # パターン内の行動の個数回す
        hit = False
        for r in record: # レコード内の行動の個数回す
            if p == r:   # パターン内とレコード内の行動が一致した場合
                # レコード内での行動が出現する位置を記録
                position.append(position_counter)
                hit = True
            position_counter += 1 # record.index(r)は使えない
        position_counter = 0
        position_stack.append(position) # position_stackにpositionを統合
        position = list() # 新たなオブジェクトとしてpositionを再生成
        if hit is False:
            return None # 一つでもヒットしないものがあればNoneを返す

    for stack in position_stack:
        if len(stack) == 1: # positionが1個の場合
            if not combination_list: # combination_listが空の場合
                for position in stack:
                    combination_list.append([position])
                    # positionを新しい要素として追加
                combination_counter = len(combination_list)
            else:
                for position in stack:
                    for c in xrange(combination_counter):
                        combination_list[c].append(position)
                        # 既存のListにpositionを追加

        elif len(stack) > 1: # stackにpositionが2個以上ある場合
            if not combination_list: # combination_listが空の場合
                for position in stack:
                    combination_list.append([position])
                    # positionを新しい要素として追加
                combination_counter = len(combination_list)
            else: # combination_listは空でない場合
                for x in xrange(len(stack)-1):
                    copies = deepcopy(combination_list)
                    for copy in copies:
                        combination_list.append(copy)
                combination_counter = len(combination_list)

                positionIndex = 0
                if len(stack) > len(copy):
                    for loop in xrange(combination_counter):
                        if loop != 0 and math.fmod(loop,len(copy)) == 0:
                            positionIndex += 1
                        combination_list[loop].append(stack[positionIndex])
                elif len(stack) < len(copy):
                    for loop in xrange(combination_counter):
                        if loop != 0 and math.fmod(loop,len(stack)) == 0:
                            positionIndex += 1
                        combination_list[loop].append(stack[positionIndex])
                elif len(stack) == len(copy):
                    for loop in xrange(combination_counter):
                        combination_list[loop].append(stack[positionIndex])
                        if loop != 0 and math.fmod(loop+1,len(copy)) == 0:
                            positionIndex += 1
    return combination_list

def getDistances(record, pattern):
    # 距離の組み合わせリストから距離を返す
    distances = list()
    prev      = -1

    combination_list = getCombinationList(record, pattern)
    if combination_list is None:
        return None
    for combination in combination_list:
        diff_sum = 0 # 計算結果を初期化
        prev = 0
        first_loop = True
        for position in combination:
            if len(combination) != 1:
                if first_loop == False and prev < position:
                # 論理的矛盾のない前後関係のみ計算
                    diff_sum += position - prev - 1
                    prev = position
                else:
                # 論理的矛盾が発生した段階で計算結果を-1とし次の組み合わせへ
                    diff_sum = False
            elif len(combination) == 1: # 要素が1個なら距離は0
                diff_sum = 0
            prev = position
            first_loop = False
        if diff_sum is not False: # 論理的矛盾でdiff_sumはFalse
            distances.append(diff_sum)
    return distances

def getDistanceList(transaction_list, pattern):
    # 全てのトランザクションについて距離を求め, パターンごとに距離リストを返す
    distance_list = [0,0,0,0,0] # あとで空のリスト生成する方法考える

    for record in transaction_list:
        distances = getDistances(record, pattern)
        if distances is not None:
            for distance in distances:
                distance_list[distance] += 1
    return distance_list

def getSubPattern(pattern):
    # 入力したパターンの部分パターンをリストで返す
    # せっかくここで部分パターンの距離求めてるんだからこの値も返したい...
    sp_list = list()

    if len(pattern) != 1: # これでいいのか？
        sp_combinations = list(combinations(pattern, len(pattern)-1))
        for sp in sp_combinations:
            sp_distance = getDistances(pattern,sp)
            if sp_distance is not None:
                sp_list.append(sp)
    return sp_list

def CountAll(distance_list):
    # パターンの全出現回数の和を返す
    count = 0

    for distance in distance_list:
        count += distance
    return count

def getDistanceRate(transaction_list, pattern):
    # パターンの距離を基に距離割合を返す
    discount   = float(1)/3 # 浮動小数点の表現のため
    index      = 0
    weight     = 1.0
    weight_sum = 0

    distance_list = getDistanceList(transaction_list, pattern)
    count = CountAll(distance_list)
    for distance in distance_list:
        weight_sum += discount**index * distance * weight
        index += 1
    return weight_sum / count

def getSupport(transaction_list, pattern):
    # パターンのサポート値を返す
    distance_list = getDistanceList(transaction_list, pattern)
    return float(CountAll(distance_list)) / len(transaction_list)

def getNeighborhood(transaction_list, pattern):
    # パターンの距離割合を基に隣接度を返す
    discount = float(1)/3 # 浮動小数点の表現のため
    neighborhood = 0

    sp_list = getSubPattern(pattern)
    if sp_list == []:
        # リストが空(=単独アイテム)なら隣接度は1
        neighborhood += 1.0
    else:
        distance_rate = getDistanceRate(transaction_list, pattern)
        for sp in sp_list:
            # サブパターンの距離をgetSubPatternで返せるようにしたい
            sp_distance = getDistances(pattern,sp)
            if len(sp) == 1:
                neighborhood += distance_rate
            else:
                sp_neigh = getNeighborhood(transaction_list,sp)
                neighborhood += discount**sp_distance * distance_rate * sp_neigh
    return neighborhood

def getScore(transaction_list, pattern):
    # パターンの推薦スコアを返す
    if len(pattern) == 1:
        score = 0
    else:
        score = getSupport(transaction_list, pattern) * getNeighborhood(transaction_list, pattern)
    return score

def test1():
    transaction_list = [
    ["Eat","Bar"],
    ["Eat","Tea","Shop","Eat","Play"],
    ["Eat","Tea","Shop","Eat","Bar"],
    ["Eat","Bar"],
    ["Shop","Eat","Play"],
    ["Play","Bar"],
    ["Eat","Bar"],
    ["Eat","Shop","Eat","Play","Bar"]
    ]

    pattern = ["Eat","Bar"]

    print "Pattern:%s" % pattern
    print "Distance Rate:%s Neighborhood:%s Score:%s" % (getDistanceRate(transaction_list, pattern),getNeighborhood(transaction_list, pattern),getScore(transaction_list, pattern))

def test2():
    record  = ["Shop","Eat","Tea","Eat","Play"]

    pattern = ["Shop"]
    print getDistances(record,pattern)

    pattern = ["Eat"]
    print getDistances(record,pattern)

    pattern = ["Shop","Eat"]
    print getDistances(record,pattern)

    pattern = ["Shop","Tea"]
    print getDistances(record,pattern)

    pattern = ["Shop","Tea","Play"]
    print getDistances(record,pattern)

    pattern = ["Shop","Eat","Play"]
    print getDistances(record,pattern)

    pattern = ["Shop","Eat","Eat"]
    print getDistances(record,pattern)

if __name__ == '__main__':
    test1()