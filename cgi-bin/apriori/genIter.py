#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
from model import model as svm
from neighborhood import neighborhood as neigh
from tools import util as util


# 類似ユーザーを抽出し逐次的に返す
def getSimUsers(user, model, user_input):
    threshold = 0.5  # 50%以上類似

    # システムから自分以外の全てのユーザーを返す(将来的にSQL導入)
    def getOtherUsers(user_input):
        other_users = list()
        A = user_input[2]
        B = user_input[3]
        if (A == "Eat" and B == "Tea") or (A == "Tea" and B == "Eat"):
            other_users = ["001", "002", "003", "004"]
        elif (A == "Eat" and B == "Play") or (A == "Play" and B == "Eat"):
            other_users = ["005", "006", "007", "008"]
        elif (A == "Eat" and B == "Sight") or (A == "Sight" and B == "Eat"):
            other_users = ["009", "010", "011", "012"]
        elif (A == "Eat" and B == "Appreciate") or (A == "Appreciate" and B == "Eat"):
            other_users = ["013", "014", "015", "016"]
        elif (A == "Eat" and B == "Shop") or (A == "Shop" and B == "Eat"):
            other_users = ["017", "018", "019", "020"]
        elif (A == "Tea" and B == "Play") or (A == "Play" and B == "Tea"):
            other_users = ["021", "022", "023", "024"]
        elif (A == "Tea" and B == "Sight") or (A == "Sight" and B == "Tea"):
            other_users = ["025", "026", "027", "028"]
        elif (A == "Tea" and B == "Appreciate") or (A == "Appreciate" and B == "Tea"):
            other_users = ["029", "030", "031", "032"]
        elif (A == "Tea" and B == "Shop") or (A == "Shop" and B == "Tea"):
            other_users = ["033", "034", "035", "036"]
        elif (A == "Play" and B == "Sight") or (A == "Sight" and B == "Play"):
            other_users = ["037", "038", "039", "040"]
        elif (A == "Play" and B == "Appreciate") or (A == "Appreciate" and B == "Play"):
            other_users = ["041", "042", "043", "044"]
        elif (A == "Play" and B == "Shop") or (A == "Shop" and B == "Play"):
            other_users = ["045", "046", "047", "048"]
        elif (A == "Sight" and B == "Shop") or (A == "Shop" and B == "Sight"):
            other_users = ["049", "050", "051", "052"]
        elif (A == "Appreciate" and B == "Shop") or (A == "Shop" and B == "Appreciate"):
            other_users = ["053", "054", "055", "056"]
        # other_users = ["001", "002", "003", "004", "005", "006", "007", "008", "013", "014", "015", "016", "017", "018", "019", "020", "021", "022", "023", "024", "029", "030", "031", "032", "033", "034", "035", "036", "041", "042", "043", "044", "045", "046", "047", "048", "053", "054", "055", "056"]
        return other_users
    other_users = getOtherUsers(user_input)
    for other_user in other_users:
        if other_user != user:
            util.convertUserDataForGenSeqModel(other_user, user_input)
            if svm.getAccuracy(other_user, model) >= threshold:
                sim_user = other_user  # わかりやすさのため書いた
                yield sim_user


# 類似ユーザーの履歴に含まれるラベル、コンテキスト、ジャンル(行動)を取得
def getHistories(sim_user):
    f = open('userData/'+sim_user+'_history.txt', 'r')
    for line in f:
        history_context = list()
        history = list()
        splited_line = line.split(', ')
        label = int(splited_line[18])
        contexts = splited_line[1:3]
        genres = splited_line[8:13]
        for context in contexts:
            history_context.append(context)
        for genre in genres:
            if genre != '0':
                history.append(genre)
        yield label, history_context, history


# 類似ユーザーの履歴から入力したlabel=1かつコンテキストに一致するもののリストを返す
def getDataIter(user, model, user_input):
    data_iter = list()
    sim_iter = list()

    # 履歴のコンテキストが適合しているか判定
    def matchContext(history_context, user_input):
        context = [user_input[0], user_input[1]]
        if context == history_context:
            return True
        else:
            return False

    for sim_user in getSimUsers(user, model, user_input):
        for label, history_context, history in getHistories(sim_user):
            if label == 1:  # 類似ユーザーが正と評価した履歴だけ推薦に利用
                if matchContext(history_context, user_input):
                    data_iter.append(history)
                    sim_iter.append(sim_user)
    return data_iter, sim_iter
