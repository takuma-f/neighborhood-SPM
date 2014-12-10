#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
import cgi
import cgitb
import random
import time

from neighborhood import neighborhood as neigh
from apriori import genPattern as apriori
from apriori import genIter as genIter
from model import model as svm
from tools import util as util


def main():
    unixtime = int(time.time())
    random.seed(unixtime)  # 乱数シードを設定(POPとrandam)
    input_data = cgi.FieldStorage()
    user = input_data["userId"].value

    # ユーザーのモデルを生成
    util.convertUserDataForGenSeqModel(user)
    model = svm.genModel(user)
    svm.saveModel(user+'.model', model)

    # 類似ユーザーの履歴から入力したコンテキストに一致するもののリストを受け取る
    data_iter, sim_iter = genIter.getDataIter(user, model, input_data)
    transaction_list, patterns = apriori.genPattern(data_iter, minSupport=0.0)

    pattern_dict = neigh.getDict(transaction_list, patterns)
    sorted_dict = sorted(pattern_dict.items(), key=lambda x: x[1])

    pattern_confDict = neigh.getConfDict(transaction_list, patterns)
    sorted_confDict = sorted(pattern_confDict.items(), key=lambda x: x[1])

    print "<!DOCTYPE html>"

# 検証用の詳細パネル(原則コメントアウト)
# ---ここから---
    print """
<div id="detail" class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">抽出データ詳細</h3>
  </div>
    <div class="panel-body">
      <div class="row">
    """
    for sim_user in genIter.getSimUsers(user, model):
      print "ユーザー:%s (類似度%s)" % (sim_user, svm.getAccuracy(sim_user, model))
      print "<br>"
      for label, history_context, history in genIter.getHistories(sim_user):
        print "抽出されたパターン :<br>"
        history = util.convertAction(history)
        for h in history:
          print "%s -> " % h
        print "<br>"
      print "<br>"
    print "コンテキストにマッチしたパターン :<br>"
    for transaction in transaction_list:
      transaction = util.convertAction(transaction)
      for t in transaction:
        print "%s -> " % t
      print "<br>"
    print """
    </div>
  </div>
</div>
    """
    conv_data_iter = list()
    for data in data_iter:
        conv_data_iter.append(util.convertAction(data))
    # print '<form id="analystic">'
    # print '<input type="hidden" id="data_iter" value="%s">' % conv_data_iter
    # print '<input type="hidden" id="sim_iter" value="%s">' % sim_iter
    # print '</form>'
# ---ここまで---

    counter = 0
    neigh_count = 0
    conf_count = 0
    display = list()
    # for p, s in sorted_dict:
    for i in xrange(1, 11):
        counter += 1
        # if counter == 1:
        #   top_score = s
        # recommend_score = 100 * (s/top_score)
        print """
<div id="plan%s" class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">おすすめプラン%s</h3>
  </div>
    <div class="panel-body">
      <div class="row">
        <form id="planForm%s">
        """ % (counter, counter, counter)

        # 乱数で入れ替える
        if random.randint(1, 2) == 1:
            if neigh_count < 3:
                p, s = sorted_dict.pop()
                while (p in display) or (len(util.convertList(p)) < 4):
                    p, s = sorted_dict.pop()
                else:
                    which = "neigh"  # 隣接度のマーカー
                    neigh_count += 1
                    display.append(p)
            else:
                p, s = sorted_confDict.pop()
                while (p in display) or (len(util.convertList(p)) < 4):
                    p, s = sorted_confDict.pop()
                else:
                  which = "conf"  # 信頼度のマーカー
                  conf_count += 1
                  display.append(p)
        else:
            if conf_count < 3:
                p, s = sorted_confDict.pop()
                while (p in display) or (len(util.convertList(p)) < 4):
                    p, s = sorted_confDict.pop()
                else:
                  which = "conf"  # 信頼度のマーカー
                  conf_count += 1
                  display.append(p)
            else:
                p, s = sorted_dict.pop()
                while (p in display) or (len(util.convertList(p)) < 4):
                    p, s = sorted_dict.pop()
                else:
                    which = "neigh"  # 隣接度のマーカー
                    neigh_count += 1
                    display.append(p)

        p = util.convertList(p)  # ここでpはlist()でなく文字列になっていることに注意
        convert_p = util.convertAction(p)
        counter_a = 0

        # 隠れ変数の定義
        print """
        <input type="hidden" id="pattern%s" value="%s">
        <input type="hidden" id="type%s" value="%s">
        <input type="hidden" id="ordPlan%s" value="%s">
        <input type="hidden" id="amount%s" value="%s">
        <input type="hidden" id="score%s" value="%s">
        <input type="hidden" id="seed" value="%s">
        """ % (counter, str(convert_p), counter, which, counter, counter, counter, len(p), counter, s, unixtime)

        for (action, a) in zip(convert_p, p):
            counter_a += 1
            print '<div class="col-md-4">'
            print '<div class="row">'
            print '<h4>%sヶ所目：%s</h4>' % (counter_a, action)
            print "</div>"
            print '<div class="row">'
            print '<div class="text-center">'
            if a == "1":
              print '<p><img src="/images/Resized256/japanese.jpg"></p>'
            elif a == "2":
              print '<p><img src="/images/Resized256/chinese.jpg"></p>'
            elif a == "3":
              print '<p><img src="/images/Resized256/yakiniku.jpg"></p>'
            elif a == "4":
              print '<p><img src="/images/Resized256/italian.jpg"></p>'
            elif a == "5":
              # <!--ファミリーレストラン-->
              print '<p><img src="/images/Resized256/famires.jpg"></p>'
            elif a == "6":
              # <!--定食-->
              print '<p><img src="/images/Resized256/ootoya.jpg"></p>'
            elif a == "7":
              print '<p><img src="/images/Resized256/curry.jpg"></p>'
            elif a == "8":
              print '<p><img src="/images/Resized256/ramen.jpg"></p>'
            elif a == "9":
              print '<p><img src="/images/Resized256/fastfood.jpg"></p>'
            elif a == "10":
              print '<p><img src="/images/Resized256/pub.jpg"></p>'
            elif a == "11":
              print '<p><img src="/images/Resized256/cafe(japanese).jpg"></p>'
            elif a == "12":
              print '<p><img src="/images/Resized256/cafe.jpg"></p>'
            elif a == "13":
              # <!--遊園地-->
              print '<p><img src="/images/Resized256/amusementpark.jpg"></p>'
            elif a == "14":
              # <!--水族館-->
              print '<p><img src="/images/Resized256/seapark.jpg"></p>'
            elif a == "15":
              # <!--映画館-->
              print '<p><img src="/images/Resized256/cinema.jpg"></p>'
            elif a == "16":
              # <!--カラオケ・ゲームセンター-->
              print '<p><img src="/images/Resized256/karaoke.jpg"></p>'
            elif a == "17":
              # <!--スポーツ施設-->
              print '<p><img src="/images/Resized256/pool.jpg"></p>'
            elif a == "18":
              # <!--レジャー施設・ビーチ-->
              print '<p><img src="/images/Resized256/camp.jpg"></p>'
            elif a == "19":
              # <!--イベント会場-->
              print '<p><img src="/images/Resized256/event.jpg"></p>'
            elif a == "20":
              # <!--温泉・リゾート施設-->
              print '<p><img src="/images/Resized256/onsen.jpg"></p>'
            elif a == "21":
              # <!--夜遊び・ディスコクラブ-->
              print '<p><img src="/images/Resized256/discoclub.jpg"></p>'
            elif a == "22":
              print '<p><img src="/images/Resized256/shrine.jpg"></p>'
            elif a == "23":
              # <!--史跡-->
              print '<p><img src="/images/Resized256/coloseum.jpg"></p>'
            elif a == "24":
              print '<p><img src="/images/Resized256/tower.jpg"></p>'
            elif a == "25":
              print '<p><img src="/images/Resized256/park.jpg"></p>'
            elif a == "26":
              # <!--博物館-->
              print '<p><img src="/images/Resized256/museum.jpg"></p>'
            elif a == "27":
              # <!--美術館-->
              print '<p><img src="/images/Resized256/gallely.jpg"></p>'
            elif a == "28":
              # <!--資料館-->
              print '<p><img src="/images/Resized256/gallely.jpg"></p>'
            elif a == "29":
              # <!--百貨店-->
              print '<p><img src="/images/Resized256/mitsukoshi.jpg"></p>'
            elif a == "30":
              # <!--ファッション-->
              print '<p><img src="/images/Resized256/fashion.jpg"></p>'
            elif a == "31":
              # <!--食品(持ち帰り)-->
              print '<p><img src="/images/Resized256/souvenir.jpg"></p>'
            elif a == "32":
              # <!--菓子(持ち帰り)-->
              print '<p><img src="/images/Resized256/sweets.jpg"></p>'
            elif a == "33":
              # <!--酒類(持ち帰り)-->
              print '<p><img src="/images/Resized256/liquorstore.jpg"></p>'
            elif a == "34":
              print '<p><img src="/images/Resized256/souvenir.jpg"></p>'
            elif a == "35":
              # 食器・花器
              print '<p><img src="/images/Resized256/tableware.jpg"></p>'
            elif a == "36":
              # 宝飾店
              print '<p><img src="/images/Resized256/jewelyshop.jpg"></p>'
            elif a == "37":
              # 書店
              print '<p><img src="/images/Resized256/bookstore.jpg"></p>'
            elif a == "38":
              # <!--家電量販店-->
              print '<p><img src="/images/Resized256/souvenir.jpg"></p>'
            elif a == "39":
              # <!--スポーツ用品店-->
              print '<p><img src="/images/Resized256/sports.jpg"></p>'
            elif a == "40":
              # <!--家具屋-->
              print '<p><img src="/images/Resized256/furniture.jpg"></p>'
            elif a == "41":
              # <!--その他趣味品-->
              print '<p><img src="/images/Resized256/akihabara.jpg"></p>'
            print "</div>"
            print "</div>"
            print "</div>"
        print """
          </form>
        </div>
      </div>
      <div class="panel-footer">
        """
        print """
        <input type="radio" form="patternForm" name="rate%s" value="1"> このプランは面白そう！
        <input type="radio" form="patternForm" name="rate%s" value="-1"> このプランはイマイチ
        """ % (counter, counter)
        if counter == 6:
          print """
        <br />
        <br />
        <button type="button" class="btn btn-primary btn-small" id="saveRating" form="planForm">
          <i class="glyphicon glyphicon-plus"></i> 評価を送信！
        </button>
          """
        print """
  </div>
</div>
        """
        if counter == 6:
            break  # 6個提示
    print """
  <script src="../js/ajaxSave.js"></script>
    """
    cgitb.enable()


if __name__ == '__main__':
    main()
