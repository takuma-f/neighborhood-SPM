# coding: UTF-8
import sys
sys.path.append('/Library/Python/2.7/site-packages/libsvm-3.17/python')
from svm import *
from svmutil import *

y,x = svm_read_problem('takuma.txt') # 学習データ入力
prob = svm_problem(y,x) # 学習データ読み込み
param = svm_parameter('-t 2 -c 1') # パラメータ設定
m = svm_train(prob,param) # 学習, 分類モデル作成
svm_save_model('model_file.svm', m) # モデルをファイルに書き出す

yt, xt = svm_read_problem('takuma.txt') # 比較対象の学習データを読み込む

p_label, p_acc, p_val = svm_predict(yt, xt, m ) #予測する
# print p_label
# print p_acc
# print p_val