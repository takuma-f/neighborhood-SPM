#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
sys.stderr = sys.stdout
import os
import datetime
import cgitb
cgitb.enable()

from cgi import escape
from tools import util as util


def main():
  today = datetime.date.today()
  print "Content-Type: text/html"
  print
  print """
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="TakumaFUJITSUKA" content="">

    <title>Perfect Planner</title>

    <!-- Bootstrap core CSS -->
    <link href="./dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="./dist/css/starter-template.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="./assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="./assets/js/ie-emulation-modes-warning.js"></script>

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="./assets/js/ie10-viewport-bug-workaround.js"></script>

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
          <li><a href="./cgi_add.cgi"><i class="glyphicon glyphicon-user"></i> 好みを入力する</a></li>
          <li class="active"><a href=""><i class="glyphicon glyphicon-heart"></i> 推薦を受ける</a></li>
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
            <h3 class="panel-title">入力した好みをもとに観光プランを推薦します！</h3>
          </div>
          <div class="panel-body">
            <div class="row">
              <div class="col-md-12">
                <input type="text" id="userId" name="userId" placeholder="ユーザーIDを入力" style="width:180px; height:30px;">
                <input type="hidden" id="date" name="date" value="%s">
  """ % today.isoformat()
  print """
<select id="situation" name="situation" style="width:190px;">
  <option value="">好みを入力した状況を選択</option>
  <option value="1">状況①: [一人, 5000円以下]</option>
  <option value="2">状況②: [一人, 5000〜10000円]</option>
  <option value="3">状況③: [一人, 10000円〜30000円]</option>
  <option value="4">状況④: [一人, 30000円以上]</option>
  <option value="5">状況⑤: [友人, 5000円以下]</option>
  <option value="6">状況⑥: [友人, 5000〜10000円]</option>
  <option value="7">状況⑦: [友人, 10000円〜30000円]</option>
  <option value="8">状況⑧: [友人, 30000円以上]</option>
  <option value="9">状況⑨: [恋人, 5000円以下]</option>
  <option value="10">状況⑩: [恋人, 5000〜10000円]</option>
  <option value="11">状況⑪: [恋人, 10000円〜30000円]</option>
  <option value="12">状況⑫: [恋人, 30000円以上]</option>
  <option value="13">状況⑬: [家族, 5000円以下]</option>
  <option value="14">状況⑭: [家族, 5000〜10000円]</option>
  <option value="15">状況⑮: [家族, 10000円〜30000円]</option>
  <option value="16">状況⑯: [家族, 30000円以上]</option>
</select>
  """
  for i in xrange(1,3):
    print """
<select id="focus%s" name="focus%s" style="width:190px;">
  <option value="0">順序を重視するジャンル%s</option>
  <optgroup label="行動: 食事する">
    <option value="Eat">和食・寿司</option>
    <option value="Eat">中華・韓国料理</option>
    <option value="Eat">焼肉・焼き物</option>
    <option value="Eat">洋食・カフェめし</option>
    <option value="Eat">定食</option>
    <option value="Eat">カレー・アジア料理</option>
    <option value="Eat">ラーメン</option>
  </optgroup>
  <optgroup label="行動: お茶する">
    <option value="Tea">カフェ・スイーツ（和風）</option>
    <option value="Tea">カフェ・スイーツ（洋風）</option>
  </optgroup>
  <optgroup label="行動: 遊ぶ">
    <option value="Play">遊園地</option>
    <option value="Play">遊園地・水族館</option>
    <option value="Play">映画館・劇場</option>
    <option value="Play">ビーチ・スキー場他レジャー施設</option>
    <option value="Play">イベント会場</option>
    <option value="Play">温泉・リゾート施設</option>
  </optgroup>
  <optgroup label="行動: 名所を見る・歩く">
    <option value="Sight">神社・仏閣</option>
    <option value="Sight">史跡</option>
    <option value="Sight">展望台・タワー</option>
    <option value="Sight">公園・庭園</option>
  </optgroup>
  <optgroup label="行動: 鑑賞する">
    <option value="Appreciate">博物館</option>
    <option value="Appreciate">美術館・ギャラリー</option>
    <option value="Appreciate">資料館・ミュージアム</option>
  </optgroup>
  <optgroup label="行動: 買物する">
    <option value="Shop">ファッション</option>
    <option value="Shop">食品（持ち帰り）</option>
    <option value="Shop">菓子（持ち帰り）</option>
    <option value="Shop">雑貨・土産物</option>
    <option value="Shop">食器・花器</option>
    <option value="Shop">宝飾品</option>
    <option value="Shop">書店</option>
  </optgroup>
</select>
    """ % (i, i, i)
  print """
              </div>
            </div>
          </div>
          <div class="panel-footer">
            <button type="button" class="btn btn-primary" id="submitContext" value="conf" style="width:150px;">プランを作る</button>
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
    <script src="./js/jquery-1.11.1.min.js"></script>
    <script src="./dist/js/bootstrap.min.js"></script>
    <script src="./assets/js/docs.min.js"></script>
    <script src="./js/ajax2.js"></script>
  """

  print "</body></html>"


if __name__ == '__main__':
  main()
