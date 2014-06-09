# coding: UTF-8
from itertools import combinations

def getDistance(record, pattern):
    # レコード一つに含まれるパターンの距離を返す
    distance_sum = 0
    p_diff       = 0
    count_p      = 0
    firsthit     = False
    hit          = False

    for p in pattern:    # パターン内の行動の個数回す
        for r in record: # レコード内の行動の個数回す
            if p == r:   # パターン内とレコード内の行動が一致した場合
                diff      = record.index(r) - pattern.index(p)
                distance  = diff - p_diff
                p_diff = diff
                if count_p == 0 and firsthit == False:
                    firsthit = True
                    distance = 0
                if firsthit == True:
                    hit = True
                distance_sum += distance
        if hit == False:
            return None
        else:
            count_p += 1
            hit = False
    return distance_sum

def getDistanceList(transactionList, pattern):
    # 全てのトランザクションについて距離を求め, パターンごとに距離リストを返す
    distance_list = [0,0,0] # とりあえずあとで空のリストでアレする方法アレ

    for record in transactionList:
        distance = getDistance(record, pattern)
        if distance is not None:
            distance_list[distance] += 1
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

if __name__ == '__main__':
    transactionList = [
    ["Eat","Bar"],
    ["Tea","Shop","Eat","Play"],
    ["Tea","Shop","Eat","Bar"],
    ["Eat","Bar"],
    ["Eat","Play"],
    ["Play","Bar"],
    ["Eat","Bar"],
    ["Shop","Eat","Play","Bar"]
    ]

    pattern = ["Tea"]
    print "Pattern:%s Distance Rate:%s Neighborhood:%s Score:%s" % (pattern,getDistanceRate(transactionList, pattern),getNeighborhood(transactionList, pattern),getScore(transactionList, pattern))

    pattern = ["Shop","Bar"]
    print "Pattern:%s Distance Rate:%s Neighborhood:%s Score:%s" % (pattern,getDistanceRate(transactionList, pattern),getNeighborhood(transactionList, pattern),getScore(transactionList, pattern))

    pattern = ["Tea","Shop","Bar"]
    print "Pattern:%s Distance Rate:%s Neighborhood:%s Score:%s" % (pattern,getDistanceRate(transactionList, pattern),getNeighborhood(transactionList, pattern),getScore(transactionList, pattern))

    pattern = ["Tea","Shop","Eat","Play"]
    print "Pattern:%s Distance Rate:%s Neighborhood:%s Score:%s" % (pattern,getDistanceRate(transactionList, pattern),getNeighborhood(transactionList, pattern),getScore(transactionList, pattern))