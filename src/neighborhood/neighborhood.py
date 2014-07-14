# coding: UTF-8
from itertools import combinations
from copy import deepcopy
import math


def getPositionStack(record, pattern):
    # 距離の組み合わせリストを返す
    position         = list()
    position_stack   = list()
    position_counter = 0

    try:
        for p in pattern:     # パターン内の行動の個数回す
            hit = False
            for r in record:  # レコード内の行動の個数回す
                if p == r:    # パターン内とレコード内の行動が一致
                    position.append(position_counter)
                    hit = True
                position_counter += 1  # record.index(r)は不可
            position_counter = 0
            position_stack.append(position)  # positionを統合
            position = list()  # 新たなオブジェクトのpositionを生成
            if hit is False:
                return None  # 一つでもヒットしなければNone
        return position_stack
    except Exception, e:
        print "Error:getPositionStack"


def getCombinationList(record, pattern):
    # 距離の組み合わせリストを返す
    combination_list    = list()
    combination_counter = 0

    position_stack = getPositionStack(record, pattern)
    try:
        if position_stack is None:
            return None
        for stack in position_stack:
            if len(stack) == 1:  # positionが1個の場合
                if not combination_list:  # combination_listが空の場合
                    for position in stack:
                        combination_list.append([position])  # positionを新しい要素として追加
                    combination_counter = len(combination_list)
                else:
                    for position in stack:
                        for c in xrange(combination_counter):
                            combination_list[c].append(position)  # 既存のListにpositionを追加

            elif len(stack) > 1:  # stackにpositionが2個以上ある場合
                if not combination_list:  # combination_listが空の場合
                    for position in stack:
                        combination_list.append([position])  # positionを新しい要素として追加
                    combination_counter = len(combination_list)
                else:
                    for x in xrange(len(stack)-1):
                        copies = deepcopy(combination_list)
                        for copy in copies:
                            combination_list.append(copy)
                    combination_counter = len(combination_list)

                    def appendPosition(combination_list, x, combination_counter):
                        position_index = 0
                        for loop in xrange(combination_counter):
                            if loop != 0 and math.fmod(loop, len(x)) == 0:
                                position_index += 1
                            combination_list[loop].append(stack[position_index])

                    if len(stack) > len(copy):
                        appendPosition(combination_list, copies, combination_counter)

                    elif len(stack) < len(copy):
                        appendPosition(combination_list, stack, combination_counter)

                    elif len(stack) == len(copy):
                        appendPosition(combination_list, copies, combination_counter)
        return combination_list
    except Exception, e:
        print "Error:getCombinationList"


def getDistances(record, pattern):
    # 距離の組み合わせリストから矛盾したものを排除し距離を格納したリストを返す
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
                    if first_loop is False and prev < position:  # 論理的矛盾のない前後関係のみ計算
                        diff_sum += position - prev - 1
                    elif first_loop is True:
                        diff_sum = False
                    else:  # 論理的矛盾が発生したら結果をFalseとし次へ
                        diff_sum = False
                        break
                elif len(combination) == 1:  # 要素が1個なら距離は0
                    diff_sum = 0
                prev = position
                first_loop = False

            if diff_sum is not False:  # 論理的矛盾でdiff_sumはFalse
                distances.append(diff_sum)

        if distances == []:
            return None
        else:
            return distances
    except Exception, e:
        print "Error:getDistances"


def getDistanceList(transaction_list, pattern):
    # 全てのトランザクションについて距離を求め, パターンごとに距離リストを返す
    # 各パターンの出現回数も同時に返す
    distance_list     = [0, 0, 0, 0, 0]  # あとで空のリスト生成する方法考える
    frequency_counter = 0

    for record in transaction_list:
        distances = getDistances(record, pattern)
        if distances is not None:
            for distance in distances:
                distance_list[distance] += 1
            frequency_counter += 1
    return distance_list, frequency_counter


def getDistanceRate(transaction_list, pattern):
    # パターンの距離を基に距離割合を返す
    discount   = float(1) / 3  # 浮動小数点の表現のため
    index      = 0
    weight     = 1.0
    weight_sum = 0

    distance_list, frequency_counter = getDistanceList(transaction_list, pattern)
    try:
        def CountAll(distance_list):
            # 入力した全履歴中におけるパターンの総出現回数の和を返す
            # 純粋な出現回数であり1レコード中何回出現しても出現するたび加算する
            count = 0
            for distance in distance_list:
                count += distance
            return count

        count = CountAll(distance_list)
        for distance in distance_list:
            weight_sum += discount**index * distance * weight
            index += 1
        return weight_sum / count
    except Exception, e:
        print "Error:getDistanceRate"


def getNeighborhood(transaction_list, pattern):
    # パターンの距離割合を基に隣接度を返す
    discount = float(1)/3  # 浮動小数点の表現のため
    neighborhood = 0

    def getSubPattern(pattern):
        # 入力したパターンの部分パターンをリストで返す
        # せっかくここで部分パターンの距離求めてるんだからこの値も返したい...
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
        except Exception, e:
            print "Error:getSubPattern"

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
    except Exception, e:
        print "Error:getNeighborhood"


def getScore(transaction_list, pattern):
    # パターンの推薦スコアを返す
    def getSupport(transaction_list, pattern):
        # パターンのサポート値を返す
        distance_list, frequency_counter = getDistanceList(transaction_list, pattern)
        return float(frequency_counter) / len(transaction_list)

    try:
        if len(pattern) == 1:
            score = 0
        else:
            score = getSupport(transaction_list, pattern) * getNeighborhood(transaction_list, pattern)
        return score
    except Exception, e:
        print "Error:getScore"


def test_getScore():
    transaction_list = [['Eat', 'Bar'], ['Eat', 'Tea', 'Shop', 'Eat', 'Play'], ['Eat', 'Tea', 'Shop', 'Eat', 'Bar'], ['Eat', 'Bar'], ['Shop', 'Eat', 'Play'], ['Play', 'Bar'], ['Eat', 'Bar'], ['Eat', 'Shop', 'Eat', 'Play', 'Bar']]

    patterns = [['Eat'], ['Bar'], ['Eat', 'Bar'], ['Tea'], ['Shop'], ['Play'], ['Eat', 'Tea'], ['Eat', 'Shop'], ['Eat', 'Eat'], ['Eat', 'Play'], ['Tea', 'Shop'], ['Tea', 'Eat'], ['Tea', 'Play'], ['Shop', 'Eat'], ['Shop', 'Play'], ['Eat', 'Tea', 'Shop'], ['Eat', 'Tea', 'Eat'], ['Eat', 'Tea', 'Play'], ['Eat', 'Shop', 'Eat'], ['Eat', 'Shop', 'Play'], ['Eat', 'Eat', 'Play'], ['Tea', 'Shop', 'Eat'], ['Tea', 'Shop', 'Play'], ['Tea', 'Eat', 'Play'], ['Shop', 'Eat', 'Play'], ['Eat', 'Tea', 'Shop', 'Eat'], ['Eat', 'Tea', 'Shop', 'Play'], ['Eat', 'Tea', 'Eat', 'Play'], ['Eat', 'Shop', 'Eat', 'Play'], ['Tea', 'Shop', 'Eat', 'Play'], ['Eat', 'Tea', 'Shop', 'Eat', 'Play'], ['Tea', 'Bar'], ['Shop', 'Bar'], ['Eat', 'Tea', 'Bar'], ['Eat', 'Shop', 'Bar'], ['Eat', 'Eat', 'Bar'], ['Tea', 'Shop', 'Bar'], ['Tea', 'Eat', 'Bar'], ['Shop', 'Eat', 'Bar'], ['Eat', 'Tea', 'Shop', 'Bar'], ['Eat', 'Tea', 'Eat', 'Bar'], ['Eat', 'Shop', 'Eat', 'Bar'], ['Tea', 'Shop', 'Eat', 'Bar'], ['Eat', 'Tea', 'Shop', 'Eat', 'Bar'], ['Play', 'Bar'], ['Eat', 'Play', 'Bar'], ['Shop', 'Play', 'Bar'], ['Eat', 'Shop', 'Play', 'Bar'], ['Eat', 'Eat', 'Play', 'Bar'], ['Shop', 'Eat', 'Play', 'Bar'], ['Eat', 'Shop', 'Eat', 'Play', 'Bar']]

    for pattern in patterns:
        print
        print "Pattern:%s" % pattern
        print "Distance List:", getDistanceList(transaction_list, pattern),
        print "DistanceRate:", round(getDistanceRate(transaction_list, pattern), 3)
        print "Neighborhood:", round(getNeighborhood(transaction_list, pattern), 3),
        print "Score:", round(getScore(transaction_list, pattern), 3)


if __name__ == '__main__':
    test_getScore()
