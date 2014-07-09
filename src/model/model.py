# coding: UTF-8
import sys
sys.path.append('/Library/Python/2.7/site-packages/libsvm-3.17/python')
from svm import *
from svmutil import *


def genModel(user):
    # ユーザー名を入れるとモデルを返す
    y, x = svm_read_problem(user+".txt")  # 学習データ入力
    prob = svm_problem(y, x)  # 学習データ読み込み
    param = svm_parameter('-t 2 -c 1')  # パラメータ設定
    model = svm_train(prob, param)  # 学習,分類モデル作成
    return model


def saveModel(modelName, model):
    # 単にオーバーライドしただけ
    svm_save_model(modelName, model)  # モデルをファイルに書き出す


def getAccuracy(compUser, model):
    # Accuracyの値のみを返す
    yt, xt = svm_read_problem(compUser+".txt")
    p_label, p_acc, p_val = svm_predict(yt, xt, model)
    return p_acc[0] / 100


def main():
    print "ユーザー名を入力 :",
    user = raw_input()
    model = genModel(user)

    print "比較対象ユーザー名を入力 :",
    compUser = raw_input()

    yt, xt = svm_read_problem(compUser+".txt")  # 比較対象の学習データを読み込む
    p_label, p_acc, p_val = svm_predict(yt, xt, model)  # 予測する

if __name__ == '__main__':
    main()
