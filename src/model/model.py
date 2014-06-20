# coding: UTF-8
import sys
sys.path.append('/Library/Python/2.7/site-packages/libsvm-3.17/python')
from svm import *
from svmutil import *

# 学習データ入力
y,x = svm_read_problem('takuma.txt')

# 学習データ読み込み
prob = svm_problem(y,x)

# パラメータ設定
param = svm_parameter('-t 1 -c 3')

# 学習, 分類モデル作成
m = svm_train(prob,param)

# モデルをファイルに書き出す
svm_save_model('model_file', m)

# 比較対象ユーザーの学習データを読み込む
yt, xt = svm_read_problem('kamui.txt')

#予測する
p_label, p_acc, p_val = svm_predict(yt, xt, m )
print p_acc