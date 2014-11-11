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
    param = svm_parameter('-t 2 -c 2048 -g 2.0')  # パラメータ設定
    model = svm_train(prob, param)  # 学習,分類モデル作成
    return model


# 単にオーバーライドしただけ
def saveModel(modelName, model):
    svm_save_model(modelName, model)  # モデルをファイルに書き出す


# Accuracyのみを返す
def getAccuracy(comp_user, model):
    yt, xt = svm_read_problem('userData/'+comp_user+'_svm.txt')
    p_label, p_acc, p_val = svm_predict(yt, xt, model)
    return p_acc[0] / 100  # p_labelとか一緒に出力するとgenIterで正常に判別されなくなる


def main():
    y, x = svm_read_problem('0140006_svm.txt')  # 学習データ読み込み
    prob = svm_problem(y, x)  # 学習データ入力
    param = svm_parameter('-t 2 -c 2.0 -g 2.0')  # パラメータ設定
    model = svm_train(prob, param)  # 学習,分類モデル作成
    saveModel('0140006_svm.model', model)
    test_name = "0140007_svm.txt"
    yt, xt = svm_read_problem(test_name)
    p_label, p_acc, p_val = svm_predict(yt, xt, model)
    print p_label, p_acc[0]

    # y, x = svm_read_problem('test2.scale')  # 学習データ読み込み
    # prob = svm_problem(y, x)  # 学習データ入力
    # param = svm_parameter('-t 0 -c 32.0')  # パラメータ設定
    # model = svm_train(prob, param)  # 学習,分類モデル作成
    # saveModel('test2_scale.model', model)
    # for i in xrange(1, 10):
    #     test_name = "test2_case"+str(i)+".scale"
    #     yt, xt = svm_read_problem(test_name)
    #     p_label, p_acc, p_val = svm_predict(yt, xt, model)
    #     print p_label, p_acc[0]

    # y, x = svm_read_problem('rbf1.txt')  # 学習データ読み込み
    # prob = svm_problem(y, x)  # 学習データ入力
    # param = svm_parameter('-t 2 -c 512 -g 0.5')  # パラメータ設定
    # model = svm_train(prob, param)  # 学習,分類モデル作成
    # saveModel('rbf1.model', model)
    # for i in xrange(1, 11):
    #     test_name = "rbf1_case"+str(i)+".txt"
    #     yt, xt = svm_read_problem(test_name)
    #     p_label, p_acc, p_val = svm_predict(yt, xt, model)
    #     print p_label, p_acc[0]

if __name__ == '__main__':
    main()
