#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Library/Python/2.7/site-packages/libsvm-3.17/python')
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
from svm import *
from svmutil import *


# ユーザー名を入れるとモデルを返す
def genModel(user):
    y, x = svm_read_problem('userData/'+user+'_svm.txt')  # 学習データ読み込み
    prob = svm_problem(y, x)  # 学習データ入力
    param = svm_parameter('-t 2 -c 64.0 -g 0.0078125')  # パラメータ設定
    model = svm_train(prob, param)  # 学習,分類モデル作成
    return model


# 単にオーバーライドしただけ
def saveModel(modelName, model):
    svm_save_model(modelName, model)  # モデルをファイルに書き出す


# Accuracyのみを返す
def getAccuracy(comp_user, model):
    yt, xt = svm_read_problem('userData/'+comp_user+'_svm.txt')
    p_label, p_acc, p_val = svm_predict(yt, xt, model)
    return p_label, p_acc[0] / 100  # p_labelとか一緒に出力するとgenIterで正常に判別されなくなる


def main():
    y, x = svm_read_problem('test001_svm.txt')  # 学習データ読み込み
    prob = svm_problem(y, x)  # 学習データ入力
    param = svm_parameter('-t 2 -c 2.0 -g 2.0')  # パラメータ設定
    # param = svm_parameter('-t 2 -c 0.03125 -g 0.0078125')  # パラメータ設定
    model = svm_train(prob, param)  # 学習,分類モデル作成
    saveModel('test001_svm.model', model)
    test_name = "0140006_svm.txt"
    yt, xt = svm_read_problem(test_name)
    p_label, p_acc, p_val = svm_predict(yt, xt, model)
    print p_label, p_acc[0]


if __name__ == '__main__':
    main()
