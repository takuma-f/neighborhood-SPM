# coding: UTF-8
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
        print record
        distance = getDistance(record, pattern)
        print "Distance =",distance
        if distance is not None:
            distance_list[distance] += 1
    return distance_list

def CountAll(transactionList, pattern):
    # パターンの出現数を返す, dist_list呼ばずに値保持して参照するだけにしたい
    # dist_list = getDistanceList(transactionList, pattern)
    # for i in len(dist_list):
    #     count += dist_list[i]
    # return count
    pass

def getDistanceRate(transactionList, pattern):
    # パターンの距離を基に距離割合を返す
    # count = CountAll(transactionList, pattern)
    # for i in count:
    #     if :
    #         weight_sum = weight_sum + discount**distance * weight
    # return dist_rate = weight_sum / countAll(transactionList, pattern)
    pass

def getNeighborhood(transactionList, pattern):
    # パターンの距離割合を基に隣接度を返す
    # dist_rate = getDistanceRate(transactionList, pattern)
    # neighborhood = dist_rate * subsetsum
    # return neighborhood
    pass

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
    pattern = ["Shop","Play"]

    print getDistanceList(transactionList,pattern)