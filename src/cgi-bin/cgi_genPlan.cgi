#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
import cgi
import cgitb
import random

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

    pattern_confDict = neigh.getConfDict(transaction_list, patterns)
    sorted_confDict = sorted(pattern_confDict.items(), key=lambda x: x[1], reverse=True)

    print "<!DOCTYPE html>"
    counter = 0
    for p, s in sorted_dict:
        counter += 1
        if counter == 1:
          top_score = s
        recommend_score = 100 * (s/top_score)
        print """
  <div class="col-md-12">
    <div id="plan%s" class="panel panel-default">
      <div class="panel-heading">
        <h3 class="panel-title">おすすめプラン%s</h3>
        <!-- このプランのおすすめ度・・・%s点 -->
      </div>
        <div class="panel-body">
          <div class="row">
            <form id="planForm%s">
        """ % (counter, counter, int(recommend_score), counter)
        p = util.convertList(p)  # ここでpはlist()でなく文字列になっていることに注意
        convert_p = util.convertAction(p)
        counter_a = 0
        print """
        <input type="hidden" id="ordPlan" value="%s">
        <input type="hidden" id="amtItem" value="%s">
        """ % (counter, len(p))
        for (action, a) in zip(convert_p, p):
            counter_a += 1
            print '<div class="col-md-4">'
            print '<div class="row">'
            print '<h4>%s %s</h4>' % (counter_a, action)
            print "</div>"
            print '<div class="row">'
            print '<input type="hidden" id="which%s" value="%s">' % (counter, counter)
            if a == "1":
              print """
              <!--和食・寿司-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">多聞</option>
                <option value="">手打ちそば処 湧水</option>
                <option value="">鰻 鈴木</option>
                <option value="">とらふぐ亭</option>
                <option value="">多助割烹</option>
                <option value="">割烹 ちよだ</option>
              </select>
              """ % (counter, counter_a)
            elif a == "2":
              print """
              <!--中華料理-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">徳翔楼</option>
                <option value="">渝園</option>
                <option value="">食神 餃子王</option>
                <option value="">海南記</option>
                <option value="">唐菜</option>
              </select>
              """ % (counter, counter_a)
            elif a == "3":
              print """
              <!--焼肉・焼き物・韓国料理-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">(卸)調布食肉センター</option>
                <option value="">スエヒロ館 調布店</option>
                <option value="">牛繁 調布店</option>
                <option value="">牛角 調布店</option>
                <option value="">ぼてぢゅう 調布パルコ店</option>
                <option value="">マッサラン</option>
                <option value="">大長今</option>
              </select>
              """ % (counter, counter_a)
            elif a == "4":
              print """
              <!--イタリアン・フレンチ他洋食-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">オステリア アルコバレーノ</option>
                <option value="">トラットリア ジリオロッソ</option>
                <option value="">CAFE BUNS</option>
                <option value="">ホノルル食堂</option>
                <option value="">あじゅーる</option>
                <option value="">洋食 クリスマス亭</option>
              </select>
              """ % (counter, counter_a)
            elif a == "5":
              print """
              <!--ファミリーレストラン-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">ジョナサン 調布駅前店</option>
                <option value="">バーミヤン 調布駅南店</option>
                <option value="">ガスト 調布店</option>
              </select>
              """ % (counter, counter_a)
            elif a == "6":
              print """
              <!--定食-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">東京エガオ食堂</option>
                <option value="">大戸屋 調布北口店</option>
                <option value="">みさと屋 野菜食堂</option>
                <option value="">長谷川</option>
                <option value="">大村庵</option>
              </select>
              """ % (counter, counter_a)
            elif a == "7":
              print """
              <!--カレー・アジア料理-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="06">スラバヤ</option>
                <option value="06">タイ・トイ</option>
                <option value="06">エムスキッチン</option>
                <option value="06">インド料理 Raja</option>
                <option value="07">アジアン タイペイ</option>
              </select>
              """ % (counter, counter_a)
            elif a == "8":
              print """
              <!--ラーメン・麺類-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">しば田</option>
                <option value="">柴崎亭</option>
                <option value="">たけちゃんにぼしらーめん 調布店</option>
                <option value="">らいおん 調布店</option>
                <option value="">ラーメン二郎 仙川店</option>
                <option value="">竹屋 調布店</option>
                <option value="">そらまめ拉麺本舗</option>
                <option value="">助格家</option>
                <option value="">たつみ</option>
                <option value="">しらたか</option>
                <option value="">千年ラーメン</option>
              </select>
              """ % (counter, counter_a)
            elif a == "9":
              print """
              <!--ファストフード・牛丼-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">フレッシュネスバーガー調布店</option>
                <option value="">モスバーガー 調布南口店</option>
                <option value="">マクドナルド 調布北口店</option>
                <option value="">てんや 調布とうきゅう店</option>
                <option value="">松屋 調布北口店</option>
                <option value="">吉野家 調布北口店</option>
                <option value="">なか卯 調布北口店</option>
              </select>
              """ % (counter, counter_a)
            elif a == "10":
              print """
              <!--居酒屋・バー-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">厨ぼうず 調布店</option>
                <option value="">肉汁餃子製作所 ダンダダン酒場</option>
                <option value="">KENNY'S</option>
                <option value="">kirakutei KIRAKUYA</option>
                <option value="">二代目 うおたま</option>
                <option value="">Yuming 108</option>
                <option value="">炉端 調風</option>
                <option value="">い志井 本店</option>
              </select>
              """ % (counter, counter_a)
            elif a == "11":
              print """
              <!--カフェ・スイーツ(和風)-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="14">あずきや 安堂</option>
                <option value=""></option>
                <option value=""></option>
                <option value=""></option>
                <option value=""></option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "12":
              print """
              <!--カフェ・スイーツ(洋風)-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">サンマロー</option>
                <option value="">TP'S Cafe</option>
                <option value="">珈琲美学 深山</option>
                <option value="">プロペラ・カフェ</option>
              </select>
              """ % (counter, counter_a)
            elif a == "13":
              print """
              <!--遊園地-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">サンリオピューロランド</option>
                <option value="">京王よみうりランド</option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "14":
              print """
              <!--水族館-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">しながわ水族館(品川)</option>
                <option value="">サンシャイン水族館(池袋)</option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "15":
              print """
              <!--映画館-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">TOHOシネマズ六本木ヒルズ</option>
                <option value=""></option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "16":
              print """
              <!--カラオケ・ゲームセンター-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value=""></option>
                <option value=""></option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "17":
              print """
              <!--スポーツ施設-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">Round1 府中店</option>
                <option value="">クライミングジム ウエストロック</option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "18":
              print """
              <!--レジャー施設・ビーチ-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">サントリー武蔵野ビール工場</option>
                <option value="">京王多摩川BBQ-VILLAGE</option>
                <option value=""></option>
                <option value=""></option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "19":
              print """
              <!--イベント会場-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="23">味の素スタジアム</option>
                <option value="">多摩川河川敷(調布市花火大会)</option>
                <option value="">京王閣競輪場</option>
                <option value="">東京競馬場</option>
              </select>
              """ % (counter, counter_a)
            elif a == "20":
              print """
              <!--温泉・リゾート施設-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">深大の湯</option>
                <option value=""></option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "21":
              print """
              <!--夜遊び・ディスコクラブ-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">Studio Coast(新木場)</option>
                <option value="">WOMB(渋谷)</option>
                <option value="">Club asia(渋谷)</option>
                <option value="">ever(青山)</option>
                <option value="">unit(代官山)</option>
              </select>
              """ % (counter, counter_a)
            elif a == "22":
              print """
              <!--神社・仏閣-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="30">深大寺</option>
                <option value=""></option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "23":
              print """
              <!--史跡-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="33">近藤勇生家</option>
                <option value="">調布基地戦跡</option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "24":
              print """
              <!--展望台・タワー-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">東京スカイツリー(押上)</option>
                <option value="">東京タワー(神谷町)</option>
                <option value="">東京都庁(新宿)</option>
              </select>
              """ % (counter, counter_a)
            elif a == "25":
              print """
              <!--公園-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">神代植物公園</option>
                <option value="">野川緑道</option>
                <option value="">調布飛行場</option>
                <option value="">国立天文台</option>
              </select>
              """ % (counter, counter_a)
            elif a == "26":
              print """
              <!--博物館-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">調布市郷土博物館</option>
                <option value="">調布市武者小路実篤記念館</option>
                <option value="">下布田遺跡・郷土博物館分室</option>
                <option value="">東京アートミュージアム</option>
                <option value="">三鷹の森ジブリ美術館</option>
              </select>
              """ % (counter, counter_a)
            elif a == "27":
              print """
              <!--美術館-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">調布市郷土博物館</option>
                <option value="">調布市武者小路実篤記念館</option>
                <option value="">下布田遺跡・郷土博物館分室</option>
                <option value="">東京アートミュージアム</option>
                <option value="">三鷹の森ジブリ美術館</option>
              </select>
              """ % (counter, counter_a)
            elif a == "28":
              print """
              <!--資料館-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">調布市郷土博物館</option>
                <option value="">調布市武者小路実篤記念館</option>
                <option value="">下布田遺跡・郷土博物館分室</option>
                <option value="">東京アートミュージアム</option>
                <option value="">三鷹の森ジブリ美術館</option>
              </select>
              """ % (counter, counter_a)
            elif a == "29":
              print """
              <!--百貨店-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">調布パルコ</option>
                <option value="">伊勢丹 府中店</option>
              </select>
              """ % (counter, counter_a)
            elif a == "30":
              print """
              <!--ファッション-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">調布パルコ</option>
                <option value="">伊勢丹 府中店</option>
                <option value="">きもの処 榮屋</option>
                <option value="">オリジナル帽子 La Rainette</option>

              </select>
              """ % (counter, counter_a)
            elif a == "31":
              print """
              <!--食品(持ち帰り)-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">西村はちみつ 調布店</option>
                <option value=""></option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "32":
              print """
              <!--菓子(持ち帰り)-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">洋菓子 EACH FAN PASTRY</option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "33":
              print """
              <!--酒類(持ち帰り)-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value=""></option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "34":
              print """
              <!--雑貨・土産物-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="56">EURO SPORT味の素スタジアム店</option>
                <option value=""></option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "35":
              print """
              <!--食器・花器-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value=""></option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "36":
              print """
              <!--宝飾店-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value=""></option>
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            elif a == "37":
              print """
              <!--書店-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">真光書店</option>
                <option value="">古書 玉椿</option>
              </select>
              """ % (counter, counter_a)
            elif a == "38":
              print """
              <!--家電量販店-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">ヨドバシカメラ(新宿)</option>
                <option value="">ヤマダ電機(新宿)</option>

              </select>
              """ % (counter, counter_a)
            elif a == "39":
              print """
              <!--スポーツ用品店-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="31">GARALLY2(新宿)</option>
                <option value="34">小田急ハルク(新宿)</option>
                <option value="35">Y's Road(新宿)</option>
              </select>
              """ % (counter, counter_a)
            elif a == "40":
              print """
              <!--家具屋-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="">IKEA立川</option>
              </select>
              """ % (counter, counter_a)
            elif a == "41":
              print """
              <!--その他趣味品-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value=""></option>
              </select>
              """ % (counter, counter_a)
            print "</div>"
            print "</div>"
        print """
          </form>
        </div>
      </div>
      <div class="panel-footer">
        <button type="button" class="btn btn-primary btn-small" id="savePlan%s" form="planForm%s" value="%s"><i class="glyphicon glyphicon-plus"></i> このプランを選択</button>
        <span id="response%s"></span>
      </div>
    </div>
  </div>
        """ % (counter, counter, counter, counter)
        if counter == 10:
            break
    print """
  <script src="../js/ajaxSave.js"></script>
    """
    cgitb.enable()


if __name__ == '__main__':
    main()
