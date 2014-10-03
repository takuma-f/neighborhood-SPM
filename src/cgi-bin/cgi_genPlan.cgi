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
    random.seed(unixtime)  # 乱数シードを固定(POPとrandam)
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
    sorted_dict = sorted(pattern_dict.items(), key=lambda x: x[1])

    pattern_confDict = neigh.getConfDict(transaction_list, patterns)
    sorted_confDict = sorted(pattern_confDict.items(), key=lambda x: x[1])

    print "<!DOCTYPE html>"
    counter = 0
    neigh_count = 0
    conf_count = 0
    display = []
    # for p, s in sorted_dict:
    for i in xrange(1, 11):
        counter += 1
        # if counter == 1:
        #   top_score = s
        # recommend_score = 100 * (s/top_score)
        print """
  <div class="col-md-12">
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
        <input type="hidden" id="which%s" value="%s">
        <input type="hidden" id="ordPlan%s" value="%s">
        <input type="hidden" id="amtItem%s" value="%s">
        <input type="hidden" id="seed" value="%s">
        """ % (counter, str(convert_p), counter, which, counter, counter, counter, len(p), unixtime)

        for (action, a) in zip(convert_p, p):
            counter_a += 1
            print '<div class="col-md-4">'
            print '<div class="row">'
            print '<h4>%s %s</h4>' % (counter_a, action)
            print "</div>"
            print '<div class="row">'
            if a == "1":
              print """
              <!--和食・寿司-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="tamon">多聞</option>
                <option value="kassui">手打ちそば処 湧水</option>
                <option value="suzuki">鰻 鈴木</option>
                <option value="torafugu">とらふぐ亭</option>
                <option value="tasuke">多助割烹</option>
                <option value="chiyoda">割烹 ちよだ</option>
              </select>
              """ % (counter, counter_a)
            elif a == "2":
              print """
              <!--中華料理-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="tokusyou">徳翔楼</option>
                <option value="yuen">渝園</option>
                <option value="syokujin">食神 餃子王</option>
                <option value="kainanki">海南記</option>
                <option value="kouna">唐菜</option>
              </select>
              """ % (counter, counter_a)
            elif a == "3":
              print """
              <!--焼肉・焼き物・韓国料理-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="syokuniku">(卸)調布食肉センター</option>
                <option value="suehiro">スエヒロ館 調布店</option>
                <option value="gyushige">牛繁 調布店</option>
                <option value="gyukaku">牛角 調布店</option>
                <option value="boteju">ぼてぢゅう 調布パルコ店</option>
                <option value="massaran">マッサラン</option>
                <option value="daityou">大長今</option>
              </select>
              """ % (counter, counter_a)
            elif a == "4":
              print """
              <!--イタリアン・フレンチ他洋食-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="aruko">オステリア アルコバレーノ</option>
                <option value="giliorosso">トラットリア ジリオロッソ</option>
                <option value="cafebuns">CAFE BUNS</option>
                <option value="honolulu">ホノルル食堂</option>
                <option value="ajuru">あじゅーる</option>
                <option value="xmastei">洋食 クリスマス亭</option>
              </select>
              """ % (counter, counter_a)
            elif a == "5":
              print """
              <!--ファミリーレストラン-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="jonasan">ジョナサン 調布駅前店</option>
                <option value="bamiyang">バーミヤン 調布駅南店</option>
                <option value="gust">ガスト 調布店</option>
              </select>
              """ % (counter, counter_a)
            elif a == "6":
              print """
              <!--定食-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="egao">東京エガオ食堂</option>
                <option value="ootoya">大戸屋 調布北口店</option>
                <option value="misato">みさと屋 野菜食堂</option>
                <option value="hasegawa">長谷川</option>
                <option value="oomura">大村庵</option>
              </select>
              """ % (counter, counter_a)
            elif a == "7":
              print """
              <!--カレー・アジア料理-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="surabaya">スラバヤ</option>
                <option value="thai">タイ・トイ</option>
                <option value="emus">エムスキッチン</option>
                <option value="raja">インド料理 Raja</option>
                <option value="taipei">アジアン タイペイ</option>
              </select>
              """ % (counter, counter_a)
            elif a == "8":
              print """
              <!--ラーメン・麺類-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="shibata">しば田</option>
                <option value="shibasaki">柴崎亭</option>
                <option value="takechang">たけちゃんにぼしらーめん 調布店</option>
                <option value="lion">らいおん 調布店</option>
                <option value="sengawajiro">ラーメン二郎 仙川店</option>
                <option value="takeya">竹屋 調布店</option>
                <option value="soramame">そらまめ拉麺本舗</option>
                <option value="sukekaku">助格家</option>
                <option value="tatsumi">たつみ</option>
                <option value="shirataka">しらたか</option>
                <option value="sennen">千年ラーメン</option>
              </select>
              """ % (counter, counter_a)
            elif a == "9":
              print """
              <!--ファストフード・牛丼-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="fleshness">フレッシュネスバーガー調布店</option>
                <option value="mos">モスバーガー 調布南口店</option>
                <option value="macdonald">マクドナルド 調布北口店</option>
                <option value="tenya">てんや 調布とうきゅう店</option>
                <option value="matsuya">松屋 調布北口店</option>
                <option value="yoshinoya">吉野家 調布北口店</option>
                <option value="nakau">なか卯 調布北口店</option>
              </select>
              """ % (counter, counter_a)
            elif a == "10":
              print """
              <!--居酒屋・バー-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="kuribouzu">厨ぼうず 調布店</option>
                <option value="dandadan">肉汁餃子製作所 ダンダダン酒場</option>
                <option value="kennys">KENNY'S</option>
                <option value="kirakuya">kirakutei KIRAKUYA</option>
                <option value="uotama">二代目 うおたま</option>
                <option value="yuming108">Yuming 108</option>
                <option value="chofuu">炉端 調風</option>
                <option value="ishi">い志井 本店</option>
              </select>
              """ % (counter, counter_a)
            elif a == "11":
              print """
              <!--カフェ・スイーツ(和風)-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="azukiya">あずきや 安堂</option>
                <option value="ameya">あめや(深大寺)</option>
              </select>
              """ % (counter, counter_a)
            elif a == "12":
              print """
              <!--カフェ・スイーツ(洋風)-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="sanmaro-">サンマロー</option>
                <option value="tpcafe">TP'S Cafe</option>
                <option value="miyama">珈琲美学 深山</option>
                <option value="propella">プロペラ・カフェ</option>
              </select>
              """ % (counter, counter_a)
            elif a == "13":
              print """
              <!--遊園地-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="sanrioland">サンリオピューロランド</option>
                <option value="yomiuriland">京王よみうりランド</option>
                <option value="tdl">東京ディズニーランド・シー</option>
              </select>
              """ % (counter, counter_a)
            elif a == "14":
              print """
              <!--水族館-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="shinasui">しながわ水族館(品川)</option>
                <option value="sunshinesui">サンシャイン水族館(池袋)</option>
                <option value="kasaiaquapark">葛西臨海公園</option>
              </select>
              """ % (counter, counter_a)
            elif a == "15":
              print """
              <!--映画館-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="tohofuchu">TOHOシネマズ府中</option>
                <option value="tohoroppongi">TOHOシネマズ六本木ヒルズ</option>
                <option value="tohoshibuya">TOHOシネマズ渋谷</option>
              </select>
              """ % (counter, counter_a)
            elif a == "16":
              print """
              <!--カラオケ・ゲームセンター-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="joypolice">東京ジョイポリス(台場)</option>
                <option value="namco">ナムコナンジャタウン(池袋)</option>
                <option value="round1">Round1 府中店</option>
                <option value="bigecho">カラオケ ビッグエコー調布南口店</option>
              </select>
              """ % (counter, counter_a)
            elif a == "17":
              print """
              <!--スポーツ施設-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="round1">Round1 府中店</option>
                <option value="westrock">クライミングジム ウエストロック</option>
                <option value="summerland">東京サマーランド(あきる野市)</option>
              </select>
              """ % (counter, counter_a)
            elif a == "18":
              print """
              <!--レジャー施設・ビーチ-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="suntorybrew">サントリー武蔵野ビール工場</option>
                <option value="bbqvillage">京王多摩川BBQ-VILLAGE</option>
                <option value="hikawacamp">氷川キャンプ場(奥多摩町)</option>
                <option value="showakinen">国営昭和記念公園</option>
                <option value="summerland">東京サマーランド(あきる野市)</option>
              </select>
              """ % (counter, counter_a)
            elif a == "19":
              print """
              <!--イベント会場-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="ajista">味の素スタジアム</option>
                <option value="tamagawahanabi">多摩川河川敷(調布市花火大会)</option>
                <option value="keiokeirin">京王閣競輪場</option>
                <option value="tokyokeiba">東京競馬場</option>
              </select>
              """ % (counter, counter_a)
            elif a == "20":
              print """
              <!--温泉・リゾート施設-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="jindaionsen">深大寺天然温泉 湯守の里</option>
                <option value="kunitachionsen">国立温泉 湯楽の里</option>
                <option value="taketori">永山健康ランド 竹取の湯</option>
              </select>
              """ % (counter, counter_a)
            elif a == "21":
              print """
              <!--夜遊び・ディスコクラブ-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="ageha">Studio Coast(新木場)</option>
                <option value="womb">WOMB(渋谷)</option>
                <option value="asia">Club asia(渋谷)</option>
                <option value="ever">ever(青山)</option>
                <option value="unit">unit(代官山)</option>
              </select>
              """ % (counter, counter_a)
            elif a == "22":
              print """
              <!--神社・仏閣-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="jindaiji">深大寺</option>
                <option value="ookuni">大国魂神社</option>
                <option value="rakuou">高尾山薬王院</option>
                <option value="takahata">高幡不動金剛寺</option>
              </select>
              """ % (counter, counter_a)
            elif a == "23":
              print """
              <!--史跡-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="kondo">近藤勇生家</option>
                <option value="chofubase">調布基地戦跡</option>
                <option value="jindaiji">深大寺</option>
                <option value="ookuni">大国魂神社</option>
                <option value="tamagawajousui">玉川上水</option>
              </select>
              """ % (counter, counter_a)
            elif a == "24":
              print """
              <!--展望台・タワー-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="skytree">東京スカイツリー(押上)</option>
                <option value="tokyotower">東京タワー(神谷町)</option>
                <option value="metrogovrnment">東京都庁(新宿)</option>
              </select>
              """ % (counter, counter_a)
            elif a == "25":
              print """
              <!--公園-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="jindaipark">神代植物公園</option>
                <option value="nogawa">野川緑道</option>
                <option value="tamagawa">多摩川河川敷</option>
                <option value="showakinen">国営昭和記念公園</option>
                <option value="chofubase">京王百草園</option>
              </select>
              """ % (counter, counter_a)
            elif a == "26":
              print """
              <!--博物館-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="kyoudo">調布市郷土博物館</option>
                <option value="saneatsu">調布市武者小路実篤記念館</option>
                <option value="shimofudaiseki">下布田遺跡・郷土博物館分室</option>
                <option value="tenmondai">国立天文台</option>
                <option value="tokyoart">東京アートミュージアム</option>
                <option value="jibri">三鷹の森ジブリ美術館</option>
              </select>
              """ % (counter, counter_a)
            elif a == "27":
              print """
              <!--美術館-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="kyoudo">調布市郷土博物館</option>
                <option value="saneatu">調布市武者小路実篤記念館</option>
                <option value="shimofudaiseki">下布田遺跡・郷土博物館分室</option>
                <option value="tenmondai">国立天文台</option>
                <option value="tokyoart">東京アートミュージアム</option>
                <option value="jiburi">三鷹の森ジブリ美術館</option>
              </select>
              """ % (counter, counter_a)
            elif a == "28":
              print """
              <!--資料館-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="kyoudo">調布市郷土博物館</option>
                <option value="saneatu">調布市武者小路実篤記念館</option>
                <option value="shimofudaiseki">下布田遺跡・郷土博物館分室</option>
                <option value="tenmondai">国立天文台</option>
                <option value="tokyoart">東京アートミュージアム</option>
                <option value="jiburi">三鷹の森ジブリ美術館</option>
              </select>
              """ % (counter, counter_a)
            elif a == "29":
              print """
              <!--百貨店-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="parco">調布パルコ</option>
                <option value="isetan">伊勢丹 府中店</option>
                <option value="keio">京王百貨店 新宿店</option>
                <option value="odakyu">小田急百貨店 新宿店</option>
                <option value="lumine">LUMINE 新宿</option>
              </select>
              """ % (counter, counter_a)
            elif a == "30":
              print """
              <!--ファッション-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="parco">調布パルコ</option>
                <option value="isetan">伊勢丹 府中店</option>
                <option value="keio">京王百貨店 新宿店</option>
                <option value="odakyu">小田急百貨店 新宿店</option>
                <option value="lumine">LUMINE 新宿</option>
                <option value="sakaeya">きもの処 榮屋</option>
                <option value="lamainette">オリジナル帽子 La Rainette</option>
              </select>
              """ % (counter, counter_a)
            elif a == "31":
              print """
              <!--食品(持ち帰り)-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="eachfanpastry">洋菓子 EACH FAN PASTRY</option>
                <option value="budoen">ブドー園</option>
                <option value="nishimura">西村はちみつ 調布店</option>
              </select>
              """ % (counter, counter_a)
            elif a == "32":
              print """
              <!--菓子(持ち帰り)-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="eachfanpastry">洋菓子 EACH FAN PASTRY</option>
                <option value="budoen">ブドー園</option>
                <option value="nishimura">西村はちみつ 調布店</option>
              </select>
              """ % (counter, counter_a)
            elif a == "33":
              print """
              <!--酒類(持ち帰り)-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="yamaguchi">リカー＆フーズ やまぐち</option>
                <option value="oguraya">小倉屋(めじろ台)</option>
                <option value="keibare">京晴(八王子)</option>
              </select>
              """ % (counter, counter_a)
            elif a == "34":
              print """
              <!--雑貨・土産物-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="ameya">あめや(深大寺)</option>
                <option value="yasaka">アジアン輸入雑貨・家具KAJA調布店</option>
                <option value="eurosport">EURO SPORT味の素スタジアム店</option>
                <option value="francfranc">Francfranc調布パルコ店</option>
              </select>
              """ % (counter, counter_a)
            elif a == "35":
              print """
              <!--食器・花器-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="francfranc">Francfranc調布パルコ店</option>
                <option value="kazuki">和食器 和季＜かずき＞</option>
              </select>
              """ % (counter, counter_a)
            elif a == "36":
              print """
              <!--宝飾店-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="housekitsutsumi">ジュエリーツツミ 調布パルコ店</option>
                <option value="housekiishi">ジュエリーイシイ 西友調布店</option>
              </select>
              """ % (counter, counter_a)
            elif a == "37":
              print """
              <!--書店-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="shinko">真光書店</option>
                <option value="tamatsubaki">古書 玉椿</option>
              </select>
              """ % (counter, counter_a)
            elif a == "38":
              print """
              <!--家電量販店-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="yodobashi">ヨドバシカメラ(新宿)</option>
                <option value="bic">ビックカメラ小田急ハルク店(新宿)</option>
                <option value="yamada">ヤマダ電機(新宿)</option>
                <option value="tsukumo">ツクモ電機(秋葉原)</option>
              </select>
              """ % (counter, counter_a)
            elif a == "39":
              print """
              <!--スポーツ用品店-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="garally2">GARALLY2(新宿)</option>
                <option value="haruku">小田急ハルク(新宿)</option>
                <option value="ysroad">Y's Road(新宿)</option>
              </select>
              """ % (counter, counter_a)
            elif a == "40":
              print """
              <!--家具屋-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="yasaka">アジアン輸入雑貨・家具KAJA調布店</option>
                <option value="ikea">IKEA立川</option>
                <option value="idc">IDC大塚家具立川</option>
                <option value="yasaka">八坂家具</option>
              </select>
              """ % (counter, counter_a)
            elif a == "41":
              print """
              <!--その他趣味品-->
              <select id="venue%s%s" size="5" style="width:250px;">
                <option value="tokensakata">刀剣坂田(日本刀販売・買い取り)</option>
                <option value="emmygangu">エミー玩具店</option>
                <option value="radiokaikan">ラジオ会館(秋葉原)</option>
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
        if counter == 6:
            break  # 6個提示
    print """
  <script src="../js/ajaxSave.js"></script>
    """
    cgitb.enable()


if __name__ == '__main__':
    main()
