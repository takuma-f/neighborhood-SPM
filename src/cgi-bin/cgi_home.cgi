#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
import os
from cgi import escape

from tools import util as util


def main():
  print "<!DOCTYPE html>"
  print
  print """
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="TakumaFUJITSUKA" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Perfect Planner</title>

    <!-- Bootstrap core CSS -->
    <link href="../dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="../dist/css/starter-template.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="../assets/js/ie-emulation-modes-warning.js"></script>

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../assets/js/ie10-viewport-bug-workaround.js"></script>

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css" rel="stylesheet" />
  </head>

  <body>

  <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
      <a class="navbar-brand" href="#">Perfect Planner</a>
      </div>
      <div class="collapse navbar-collapse">
        <ul class="nav navbar-nav">
          <li class="active"><a href=""><i class="glyphicon glyphicon-home"></i> 推薦を受ける</a></li>
          <li><a href="./cgi_add.cgi"><i class="glyphicon glyphicon-plus-sign"></i> モデルを作る</a></li>
        </ul>
      </div><!--/.nav-collapse -->
    </div>
  </div>
  <div class="container">
    <form action="#">
      <br>
      <div class="row">
        <div id="inputContext" class="panel panel-default">
          <div class="panel-heading">
            <h3 class="panel-title">作成したモデルをもとに推薦を行います！</h3>
          </div>
          <div class="panel-body">
            <div class="row">
              <div class="col-md-2">
                <input type="text" id="userId" name="userId" placeholder="ユーザーIDを入力" style="width:150px; height:30px;">
                <br />
                <input type="date" id="date" name="date" style="width:150px; height:30px;">
              </div>
              <div class="col-md-2">
                <select id="companion" name="companion" style="width:150px;">
                  <option value="">同伴者を選択して下さい</option>
                  <option value="1">一人</option>
                  <option value="2">友人</option>
                  <option value="3">恋人</option>
                  <option value="4">家族</option>
                </select>
                <br />
                <br />
                <select id="budget" name="budget" style="width:150px;">
                  <option value="">予算を選択して下さい</option>
                  <option value="1">5000円以下</option>
                  <option value="2">5000 ~ 10000円</option>
                  <option value="3">10000 ~ 30000円</option>
                  <option value="4">30000円以上</option>
                </select>
              </div>
              <div class="col-md-2">
                <select id="action1" name="action1" style="width:180px;">
                  <option value="0">行動を選択</option>
                  <option value="Eat">食事する</option>
                  <option value="Tea">お茶する</option>
                  <option value="Play">遊ぶ</option>
                  <option value="Sight">名所を見る・歩く</option>
                  <option value="Appreciate">鑑賞する</option>
                  <option value="Shop">買い物する</option>
                </select>
                <br />
                <br />
                <select id="focus1" name="focus1" style="width:180px;">
                  <option value="0">重視するジャンル1</option>
                  <optgroup label="Eat">
                    <option value="Eat">和食・寿司</option>
                    <option value="Eat">中華・韓国料理</option>
                    <option value="Eat">焼肉・焼き物</option>
                    <option value="Eat">洋食・カフェめし</option>
                    <option value="Eat">定食</option>
                    <option value="Eat">カレー・アジア料理</option>
                    <option value="Eat">ラーメン</option>
                  </optgroup>
                  <optgroup label="Tea">
                    <option value="Tea">カフェ・スイーツ（和風）</option>
                    <option value="Tea">カフェ・スイーツ（洋風）</option>
                  </optgroup>
                  <optgroup label="Play">
                    <option value="Play">遊園地</option>
                    <option value="Play">水族館</option>
                    <option value="Play">映画館・劇場</option>
                    <option value="Play">ビーチ・スキー場他レジャー施設</option>
                    <option value="Play">イベント会場</option>
                    <option value="Play">温泉・リゾート施設</option>
                  </optgroup>
                  <optgroup label="Sight">
                    <option value="Sight">神社・仏閣</option>
                    <option value="Sight">史跡</option>
                    <option value="Sight">展望台・タワー</option>
                    <option value="Sight">公園・庭園</option>
                  </optgroup>
                  <optgroup label="Appreciate">
                    <option value="Appreciate">博物館</option>
                    <option value="Appreciate">美術館・ギャラリー</option>
                    <option value="Appreciate">資料館・ミュージアム</option>
                  </optgroup>
                  <optgroup label="Shop">
                    <option value="Shop">ファッション</option>
                    <option value="Shop">食品（持ち帰り）</option>
                    <option value="Shop">菓子（持ち帰り）</option>
                    <option value="Shop">雑貨・土産物</option>
                    <option value="Shop">食器・花器</option>
                    <option value="Shop">宝飾品</option>
                    <option value="Shop">書店</option>
                  </optgroup>
                </select>
              </div>
              <div class="col-md-2">
                <select id="action2" name="action2" style="width:180px;">
                  <option value="0">行動を選択</option>
                  <option value="Eat">食事する</option>
                  <option value="Tea">お茶する</option>
                  <option value="Play">遊ぶ</option>
                  <option value="Sight">名所を見る・歩く</option>
                  <option value="Appreciate">鑑賞する</option>
                  <option value="Shop">買い物する</option>
                </select>
                <br />
                <br />
                <select id="focus2" name="focus2" style="width:180px;">
                  <option value="0">重視するジャンル2</option>
                  <optgroup label="Eat">
                    <option value="Eat">和食・寿司</option>
                    <option value="Eat">中華・韓国料理</option>
                    <option value="Eat">焼肉・焼き物</option>
                    <option value="Eat">洋食・カフェめし</option>
                    <option value="Eat">定食</option>
                    <option value="Eat">カレー・アジア料理</option>
                    <option value="Eat">ラーメン</option>
                  </optgroup>
                  <optgroup label="Tea">
                    <option value="Tea">カフェ・スイーツ（和風）</option>
                    <option value="Tea">カフェ・スイーツ（洋風）</option>
                  </optgroup>
                  <optgroup label="Play">
                    <option value="Play">遊園地</option>
                    <option value="Play">水族館</option>
                    <option value="Play">映画館・劇場</option>
                    <option value="Play">ビーチ・スキー場他レジャー施設</option>
                    <option value="Play">イベント会場</option>
                    <option value="Play">温泉・リゾート施設</option>
                  </optgroup>
                  <optgroup label="Sight">
                    <option value="Sight">神社・仏閣</option>
                    <option value="Sight">史跡</option>
                    <option value="Sight">展望台・タワー</option>
                    <option value="Sight">公園・庭園</option>
                  </optgroup>
                  <optgroup label="Appreciate">
                    <option value="Appreciate">博物館</option>
                    <option value="Appreciate">美術館・ギャラリー</option>
                    <option value="Appreciate">資料館・ミュージアム</option>
                  </optgroup>
                  <optgroup label="Shop">
                    <option value="Shop">ファッション</option>
                    <option value="Shop">食品（持ち帰り）</option>
                    <option value="Shop">菓子（持ち帰り）</option>
                    <option value="Shop">雑貨・土産物</option>
                    <option value="Shop">食器・花器</option>
                    <option value="Shop">宝飾品</option>
                    <option value="Shop">書店</option>
                  </optgroup>
                </select>
              </div>
            </div>
          </div>
          <div class="panel-footer">
            <button type="button" class="btn btn-primary" id="submitContext" style="width:150px;">プランを作る</button>
            <button type="reset" class="btn btn-default" id="resetContext" style="width:150px;">条件をリセット</button>
            <span id="requestResponse"></span>
          </div>
        </div>
      </div>
    </form>
  <div id="planArea" class="row"></div>
  </div>
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="../js/jquery-1.11.1.min.js"></script>
    <script src="../dist/js/bootstrap.min.js"></script>
    <script src="../assets/js/docs.min.js"></script>
    <script src="../js/ajax2.js"></script>
    <script src="../js/ConnectedSelect.js"></script><!-- 行動とジャンルの連動プルダウン -->
  """
  # ConnectedSelect.jsの関連付けを初期化
  print "<script>"
  for x in xrange(1,3):
    print "ConnectedSelect(['action%s','focus%s']);" % (x, x)
  print "</script>"

  print "</body></html>"
  import cgitb
  cgitb.enable()


if __name__ == '__main__':
  main()
