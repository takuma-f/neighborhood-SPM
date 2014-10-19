#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
from model import model as svm


# 類似ユーザーを抽出し逐次的に返す
def getSimUsers(user, model):
    # threshold = 0.6  # 過半数超えていれば類似していると判断してよいだろう
    threshold = 0.0  # 検証用


    # システムから自分以外の全てのユーザーを返す(SQL導入後はSQLアクセス)
    def getOtherUsers():
        other_users = list()
        # other_users = ["0140001", "0140002", "0140003", "0140004", "0140005", "0140006", "0140007", "0140008", "0140009", "0140010"]
        other_users = ["0140006", "0140007", "0140008", "0140009"]
        return other_users

    other_users = getOtherUsers()
    for other_user in other_users:
        # if other_user != user:
        #     # 他ユーザーのモデルが生成されていない場合生成すべきか？
        #     if svm.getAccuracy(other_user, model) > threshold:
        #         sim_user = other_user  # わかりやすさのため書いた
        #         yield sim_user
        if svm.getAccuracy(other_user, model) > threshold:
            sim_user = other_user  # わかりやすさのため書いた
            yield sim_user


# 類似ユーザーの履歴に含まれるコンテキストとジャンル(行動)を取得
def getHistories(sim_user):
    f = open('userData/'+sim_user+'_history.txt', 'r')
    for line in f:
        history_context = list()
        history = list()
        splited_line = line.split(', ')
        contexts = splited_line[1:3]
        genres = splited_line[8:13]
        # actions = splited_line[13:18]
        for context in contexts:
            history_context.append(context)
        for genre in genres:
            if genre != '0':
                history.append(genre)
        # for action in actions:
        #     if action != '0':
        #         history.append(action)
        yield history_context, history


# 履歴のコンテキストが適合しているか判定
def matchContext(history_context, input_data):

    # 入力されたユーザー情報を処理可能な形式に変換する
    def convertInputContext(input_data):
        converted_input = list()
        converted_input.append(input_data["companion"].value)
        converted_input.append(input_data["budget"].value)
        return converted_input

    context = convertInputContext(input_data)
    if context == history_context:
        return True
    else:
        return False


# 類似ユーザーの履歴から入力したコンテキストに一致するもののリストを返す
def getDataIter(user, model, input_data):
    data_iter = list()
    sim_iter = list()

    for sim_user in getSimUsers(user, model):
        for history_context, history in getHistories(sim_user):
            if matchContext(history_context, input_data):
                data_iter.append(history)
                sim_iter.append(sim_user)
    return data_iter, sim_iter
