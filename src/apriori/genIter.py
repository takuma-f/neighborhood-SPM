#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
from model import model as svm


def getSimUsers(user, model):
    # 類似ユーザーを抽出し逐次的に返す
    threshold = 0.5

    def getOtherUsers():
        # システムから自分以外の全てのユーザーを返す(SQL導入後はSQLアクセス)
        other_users = list()

        other_users = ["0140001", "0140002"]
        return other_users

    other_users = getOtherUsers()
    for other_user in other_users:
        if other_user != user:
            # 他ユーザーのモデルが生成されていない場合生成すべきか？
            if svm.getAccuracy(other_user, model) > threshold:
                sim_user = other_user  # わかりやすさのため書いた
                yield sim_user


def getHistories(sim_user):
    # 類似ユーザーの履歴に含まれるコンテキストと行動を取得
    f = open('userData/'+sim_user+'_history.txt', 'r')
    for line in f:
        history_context = list()
        history = list()
        splited_line = line.split(', ')
        contexts = splited_line[1:3]
        actions = splited_line[13:18]
        for context in contexts:
            history_context.append(context)
        for action in actions:
            if action != '0':
                history.append(action)
        yield history_context, history


def matchContext(history_context, input_data):
    # 履歴のコンテキストが適合しているか判定
    def convertInputContext(input_data):
        # 入力されたユーザー情報を処理可能な形式に変換する
        converted_input = list()

        converted_input.append(input_data["companion"].value)
        converted_input.append(input_data["budget"].value)
        return converted_input

    context = convertInputContext(input_data)
    if context == history_context:
        return True
    else:
        return False


def getDataIter(user, model, input_data):
    # 類似ユーザーの履歴から入力したコンテキストに一致するもののリストを返す
    data_iter = list()

    for sim_user in getSimUsers(user, model):
        for history_context, history in getHistories(sim_user):
            if matchContext(history_context, input_data):
                data_iter.append(history)
    return data_iter
