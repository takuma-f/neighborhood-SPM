#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
import datetime
import os
from cgi import escape


def main():
  today = datetime.date.today()
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
          <a class="navbar-brand" href="">Perfect Planner</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href=""><i class="glyphicon glyphicon-user"></i> モデルを作る</a></li>
            <li><a href="cgi_home.cgi"><i class="glyphicon glyphicon-heart"></i> 推薦を受ける</a></li>
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
              <h3 class="panel-title">入力をもとにあなたのモデルを作成します！</h3>
            </div>
            <div class="panel-body">
              <div class="row">
                <div class="col-md-12">
                  <input type="text" id="userId" name="userId" placeholder="ユーザーIDを入力" style="width:180px; height:30px;">
                  <input type="hidden" id="date" name="date" value="%s">
                  <select id="companion" name="companion" style="width:180px;">
                    <option value="">同伴者を選択して下さい</option>
                    <option value="1">一人</option>
                    <option value="2">友人</option>
                    <option value="3">恋人</option>
                    <option value="4">家族</option>
                  </select>
                  <select id="budget" name="budget" style="width:180px;">
                    <option value="">予算を選択して下さい</option>
                    <option value="1">5000円以下</option>
                    <option value="2">5000 ~ 10000円</option>
                    <option value="3">10000 ~ 30000円</option>
                    <option value="4">30000円以上</option>
                  </select>
                </div>
              </div>
            <div class="row">
              <br/>
              <div class="col-md-1"></div>
  """ % today.isoformat()

  for x in xrange(1,6):
    print """
    <div class="col-md-2" id="ItemBox">
      <select id="genre%s" name="genre%s" style="width:180px;">
        <option value="0">ジャンルを選択</option>
        <optgroup label="行動: 食事する">
          <option value="1">和食・寿司</option>
          <option value="2">中華・韓国料理</option>
          <option value="3">焼肉・焼き物</option>
          <option value="4">洋食・カフェめし</option>
          <option value="6">定食</option>
          <option value="7">カレー・アジア料理</option>
          <option value="8">ラーメン</option>
        </optgroup>
        <optgroup label="行動: お茶する">
          <option value="11">カフェ・スイーツ（和風）</option>
          <option value="12">カフェ・スイーツ（洋風）</option>
        </optgroup>
        <optgroup label="行動: 遊ぶ">
          <option value="13">遊園地</option>
          <option value="14">水族館</option>
          <option value="15">映画館・劇場</option>
          <option value="18">ビーチ・スキー場他レジャー施設</option>
          <option value="19">イベント会場</option>
          <option value="20">温泉・リゾート施設</option>
        </optgroup>
        <optgroup label="行動: 名所を見る・歩く">
          <option value="22">神社・仏閣</option>
          <option value="23">史跡</option>
          <option value="24">展望台・タワー</option>
          <option value="25">公園・庭園</option>
        </optgroup>
        <optgroup label="行動: 鑑賞する">
          <option value="26">博物館</option>
          <option value="27">美術館・ギャラリー</option>
          <option value="28">資料館・ミュージアム</option>
        </optgroup>
        <optgroup label="行動: 買物する">
          <option value="30">ファッション</option>
          <option value="31">食品（持ち帰り）</option>
          <option value="32">菓子（持ち帰り）</option>
          <option value="34">雑貨・土産物</option>
          <option value="35">食器・花器</option>
          <option value="36">宝飾品</option>
          <option value="37">書店</option>
        </optgroup>
      </select>
    </div>
    """ % (x,x)

  print """
          </div>
        </div>
        <div class="panel-footer">
          <button type="button" class="btn btn-primary" id="genPattern" style="width:150px;">行動パターン生成！</button>
          <div id="sendResponse"></div>
        </div>
      </div>
    </div>
  </form>
  <div id="patternArea" class="row"></div>
</div>

<!-- Bootstrap core JavaScript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="../dist/js/bootstrap.min.js"></script>
<script src="../assets/js/docs.min.js"></script>
<script src="../js/ajax2.js"></script>
  """

  print "</body></html>"
  import cgitb
  cgitb.enable()


if __name__ == '__main__':
  main()
