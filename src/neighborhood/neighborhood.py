# coding: UTF-8
from itertools import combinations
from copy import deepcopy

def getDistance(record, pattern):
#     # 距離の組み合わせリストから距離を返す
#     pass

# def getCombinationList(record, pattern):
    # 距離の組み合わせリストを返す
    distance           = list()
    position           = list()
    positionStack      = list()
    combinationList    = list()
    positionCounter    = 0
    combinationCounter = 0

    for p in pattern:    # パターン内の行動の個数回す
        hit = False
        for r in record: # レコード内の行動の個数回す
            if p == r:   # パターン内とレコード内の行動が一致した場合
                # レコード内での行動が出現する位置を記録
                position.append(positionCounter)
                hit = True
            positionCounter += 1 # record.index(r)は使えない
        positionCounter = 0
        positionStack.append(position) # positionStackにpositionを統合
        position = list() # 新たなオブジェクトとしてpositionを再生成
    if hit is False:
        return None # 一つでもヒットしないものがあればNoneを返す

    print positionStack

    for stack in positionStack:
        if len(stack) == 1: # positionが1個の場合
            if not combinationList: # combinationListが空の場合
                for position in stack:
                    combinationList.append([position])
                    # positionを新しい要素として追加
            else:
                for position in stack:
                    for c in xrange(combinationCounter):
                        combinationList[c].append(position)
                        # 既存のListにpositionを追加

        elif len(stack) > 1: # stackにpositionが2個以上ある場合
            if not combinationList: # combinationListが空の場合
                for position in stack:
                    combinationList.append([position])
                combinationCounter = len(combinationList)
            else: # ここが一番大事
                for x in xrange(len(stack)-1):
                    copies = deepcopy(combinationList)
                    for copy in copies: # 
                        combinationList.append(copy)
                combinationCounter = len(combinationList)

                # ここがうまく動かねえ
                for position in stack:
                    for c in xrange(combinationCounter):
                        combinationList[c].append(position)
    print combinationList
    return combinationList

def getDistanceList(transactionList, pattern):
    # 全てのトランザクションについて距離を求め, パターンごとに距離リストを返す
    distance_list = [0,0,0,0,0]
    # とりあえずあとで空のリストでアレする方法アレ

    for record in transactionList:
        distance = getDistance(record, pattern)
        if distance is not None:
            for d in distance:
                distance_list[d] += 1
    return distance_list

def CountAll(distance_list):
    # パターンの全出現回数の和を返す
    count = 0

    for distance in distance_list:
        count += distance
    return count

def getDistanceRate(transactionList, pattern):
    # パターンの距離を基に距離割合を返す
    discount   = float(1)/3 # 浮動小数点の表現のため
    index      = 0
    weight     = 1.0
    weight_sum = 0

    distance_list = getDistanceList(transactionList, pattern)
    count = CountAll(distance_list)
    for distance in distance_list:
        weight_sum += discount**index * distance * weight
        index += 1
    return weight_sum / count

def getSubPattern(pattern):
    # 入力したパターンの部分パターンをリストで返す
    # せっかくここで部分パターンの距離求めてるんだからこの値も返したい...
    sp_list = list()
    if len(pattern) != 1: # これでいいのか？
        sp_combinations = list(combinations(pattern, len(pattern)-1))
        for sp in sp_combinations:
            sp_distance = getDistance(pattern,sp)
            if sp_distance is not None:
                sp_list.append(sp)
    return sp_list

def getNeighborhood(transactionList, pattern):
    # パターンの距離割合を基に隣接度を返す
    discount = float(1)/3 # 浮動小数点の表現のため
    neighborhood = 0

    sp_list = getSubPattern(pattern)
    if sp_list == []:
        # リストが空(=単独アイテム)なら隣接度は1
        neighborhood += 1.0
    else:
        distance_rate = getDistanceRate(transactionList, pattern)
        for sp in sp_list:
            # サブパターンの距離をgetSubPatternで返せるようにしたい
            sp_distance = getDistance(pattern,sp)
            if len(sp) == 1:
                neighborhood += distance_rate
            else:
                sp_neigh = getNeighborhood(transactionList,sp)
                neighborhood += discount**sp_distance * distance_rate * sp_neigh
    return neighborhood

def getSupport(transactionList, pattern):
    # パターンのサポート値を返す
    distance_list = getDistanceList(transactionList, pattern)
    return float(CountAll(distance_list)) / len(transactionList)

def getScore(transactionList, pattern):
    # パターンの推薦スコアを返す
    if len(pattern) == 1:
        score = 0
    else:
        score = getSupport(transactionList, pattern) * getNeighborhood(transactionList, pattern)
    return score

# def main():
#     transactionList = [
#     ["Eat","Bar"],
#     ["Eat","Tea","Shop","Eat","Play"],
#     ["Eat","Tea","Shop","Eat","Bar"],
#     ["Eat","Bar"],
#     ["Shop","Eat","Play"],
#     ["Play","Bar"],
#     ["Eat","Bar"],
#     ["Eat","Shop","Eat","Play","Bar"]
#     ]

#     pattern = ["Eat","Bar"]
#     print "Pattern:%s" % pattern
#     print "Distance Rate:%s Neighborhood:%s Score:%s" % (getDistanceRate(transactionList, pattern),getNeighborhood(transactionList, pattern),getScore(transactionList, pattern))

def main():
    record = ["Shop","Eat","Tea","Eat","Play"]
    pattern = ["Eat","Tea","Eat"]
    getDistance(record,pattern)

if __name__ == '__main__':
    main()