#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
import cgi
import cgitb

from neighborhood import neighborhood as neigh
from apriori import genPattern as apriori
from apriori import genIter as genIter
from model import model as svm
from tools import util as util


def main():
    input_data = cgi.FieldStorage()
    user = input_data["userId"].value

    # ユーザーのモデルを生成
    util.convertUserDataForGenModel(user)
    model = svm.genModel(user)
    svm.saveModel(user+'.model', model)

    # 類似ユーザーの履歴から入力したコンテキストに一致するもののリストを受け取る
    data_iter = genIter.getDataIter(user, model, input_data)
    transaction_list, patterns = apriori.genPattern(data_iter, minSupport=0.0)
    pattern_dict = neigh.getDict(transaction_list, patterns)
    sorted_dict = sorted(pattern_dict.items(), key=lambda x: x[1], reverse=True)

    # json_pattern_dict = json.dumps(pattern_dict)
    # print 'Content-Type: application/json\n\n'

    print "<!DOCTYPE html>"
    counter = 0
    for p, s in sorted_dict:
        counter += 1
        print """
        <div class="col-md-12">
          <div id="plan%s" class="panel panel-default">
            <div class="panel-heading">
              <h3 class="panel-title">おすすめプラン%s</h3>
              このプランのおすすめ度・・・
            </div>
            <div class="panel-body">
              <div class="container">
        """ % (counter, counter)
        # ここでpはlist()でなく文字列になっていることに注意
        p = util.convertList(p)
        convert_p = util.convertAction(p)
        for (action, a) in zip(convert_p, p):
            print '<div class="col-md-2">'
            print '<div class="row">'
            print action
            print "</div>"
            print '<div class="row">'
            if a == "Eat":
              print """
              <select name="action%s" size="5" style="width:150px;">
                <option value="00">手打ちそば処 湧水</option>
                <option value="02">鰻 鈴木</option>
                <option value="02">らーめん竹屋 調布店</option>
                <option value="02">千年ラーメン</option>
                <option value="02">柴崎亭</option>
                <option value="02">ラーメン二郎 仙川店</option>
                <option value="03">インド料理 Raja</option>
                <option value="03">アジアン タイペイ</option>
                <option value="03">CAFE BUNS</option>
                <option value="03">オステリア アルコバレーノ</option>
                <option value="03">トラットリア ジリオロッソ</option>
                <option value="03">洋食 クリスマス亭</option>
                <option value="01">京王多摩川BBQ-VILLAGE</option>
                <option value="01">厨ぼうず 調布店</option>
                <option value="01">KENNY'S</option>
                <option value="01">kirakutei KIRAKUYA</option>
              </select>
              """
            elif a == "Tea":
              print """
              <select name="action%s" size="5" style="width:150px;">
                <option value="10">サンマロー</option>
                <option value="10">TP'S Cafe</option>
                <option value="10">珈琲美学 深山</option>
                <option value="10">プロペラ・カフェ</option>
                <option value="10">あずきや 安堂</option>
              </select>
              """
            elif a == "Play":
              print """
              <select name="action%s" size="5" style="width:150px;">
                <option value="20">サンリオピューロランド</option>
                <option value="21">京王よみうりランド</option>
                <option value="22">サントリー武蔵野ビール工場</option>
                <option value="22">味の素スタジアム</option>
              </select>
              """
            elif a == "Sight":
              print """
              <select name="action%s" size="5" style="width:150px;">
                <option value="30">深大寺</option>
                <option value="40">神代植物公園</option>
                <option value="40">天神通り</option>
                <option value="40">近藤勇生家</option>
                <option value="31">調布飛行場</option>
                <option value="40">国立天文台</option>
              </select>
              """
            elif a == "Appreciate":
              print """
              <select name="action%s" size="5" style="width:150px;">
                <option value="40">調布市武者小路実篤記念館</option>
                <option value="40">下布田遺跡・郷土博物館分室</option>
                <option value="40">東京アートミュージアム</option>
              </select>
              """
            elif a == "Shop":
              print """
              <select name="action%s" size="5" style="width:150px;">
                <option value="50">調布パルコ</option>
                <option value="50">西村はちみつ 調布店</option>
                <option value="50">きもの処 榮屋</option>
                <option value="50">古書 玉椿</option>
                <option value="50">オリジナル帽子 La Rainette</option>
                <option value="50">洋菓子 EACH FAN PASTRY</option>
                <option value="50">EURO SPORT味の素スタジアム店</option>
              </select>
              """
            print "</div>"
            print "</div>"
        print """
      </div>
    </div>
    <div class="panel-footer">
      <button type="button" class="btn btn-primary btn-small" id="like">
        <i class="glyphicon glyphicon-plus"></i> このプランを保存
      </button>
      <button type="button" class="btn btn-default btn-small" id="like">
        <i class="glyphicon glyphicon-share"></i> シェア
      </button>
    </div>
  </div>
</div>
        """
        if counter == 5:
            break

    cgitb.enable()


if __name__ == '__main__':
    main()
