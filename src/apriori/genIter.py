#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
from model import model as svm
from tools import util as util


# 類似ユーザーを抽出し逐次的に返す
def getSimUsers(user, model, context):
    threshold = 0.7  # 過半数超えていれば類似していると判断してよいだろう

    # システムから自分以外の全てのユーザーを返す(将来的にSQL導入)
    def getOtherUsers():
        other_users = list()
        other_users = ["001", "002", "003", "004"]
        # other_users = ["test001", "test002", "test003", "test004", "test005", "test006", "test007", "test008"]
        return other_users

    other_users = getOtherUsers()
    for other_user in other_users:
        # if other_user != user:
        util.convertUserDataForGenSeqModel(other_user, context)
        if svm.getAccuracy(other_user, model) > threshold:
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
def getDataIter(user, model, context):
    data_iter = list()
    sim_iter = list()

    # 履歴のコンテキストが適合しているか判定
    # def matchContext(history_context, input_data):
    def matchContext(history_context, context):
        if context == history_context:
            return True
        else:
            return False

    for sim_user in getSimUsers(user, model, context):
        for label, history_context, history in getHistories(sim_user):
            if label == 1:  # 類似ユーザーが正と評価した履歴だけ推薦に利用
                if matchContext(history_context, context):
                    data_iter.append(history)
                    sim_iter.append(sim_user)
    return data_iter, sim_iter
