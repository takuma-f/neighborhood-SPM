#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
import os
from cgi import escape


def main():
  print "<!DOCTYPE html>"
  print
  print """
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="素晴らしくNice choice.な">
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
            <li><a href="cgi_home.cgi"><i class="glyphicon glyphicon-home"></i> プラン作成</a></li>
            <li class="active"><a href=""><i class="glyphicon glyphicon-plus-sign"></i> 情報を登録する</a></li>
            <li><a href="./cgi_viewplan.cgi"><i class="glyphicon glyphicon-list"></i> 保存したプランを見る</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">その他<span class="caret"></span></a>
              <ul class="dropdown-menu" role="menu">
                <li><a href="#">アカウント設定</a></li>
                <li class="divider"></li>
                <!-- <li class="dropdown-header"></li> -->
                <li><a href="#">Sign off</a></li>
              </ul>
            </li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>
    <div class="container">
      <form action="#">
        <br>
        <div class="row">
          <div class="col-md-10">
            <div id="plan%s" class="panel panel-default">
              <div class="panel-heading">
                <h3 class="panel-title">履歴を入力！</h3>
              </div>
              <div class="panel-body">
                <div class="row">
  """

  for x in xrange(1,6):
    print """
    <div class="col-md-3">
      <div class="col-md-12" id="ItemBox">
        <input type="text" id="venue%s" placeholder="%s箇所目に訪れた場所"/>
        <br>
        <br>
        <select id="action%s" name="action%s" style="width:150px;">
          <option value="0">取った行動を選択</option>
          <option value="Eat">食事する</option>
          <option value="Tea">お茶する</option>
          <option value="Play">遊ぶ</option>
          <option value="Sight">名所を見る・歩く</option>
          <option value="Appreciate">鑑賞する</option>
          <option value="Shop">買い物する</option>
        </select>
        <br>
        <br>
        <select id="genre%s" name="genre%s" style="width:150px;">
          <option value="0">施設のジャンルを選択</option>
          <optgroup label="Eat">
            <option value="1">寿司・和食</option>
            <option value="2">中華料理</option>
            <option value="3">焼肉・韓国料理</option>
            <option value="4">イタリアン</option>
            <option value="5">フレンチ</option>
            <option value="6">他洋食</option>
            <option value="7">カレー・アジア料理</option>
            <option value="8">ラーメン・麺類</option>
            <option value="9">ファストフード・牛丼・定食</option>
            <option value="10">居酒屋・バー</option>
          </optgroup>
          <optgroup label="Tea">
            <option value="11">カフェ・スイーツ(和風)</option>
            <option value="12">カフェ・スイーツ(洋風)</option>
          </optgroup>
          <optgroup label="Play">
            <option value="13">遊園地</option>
            <option value="14">水族館</option>
            <option value="15">映画館</option>
            <option value="16">カラオケ・ゲームセンター</option>
            <option value="17">スポーツ施設</option>
            <option value="18">アウトドアレジャー施設</option>
            <option value="19">イベント会場</option>
            <option value="20">温泉・リゾート施設</option>
            <option value="21">夜遊び・ディスコクラブ</option>
          </optgroup>
          <optgroup label="Sight">
            <option value="22">神社・仏閣</option>
            <option value="23">史跡</option>
            <option value="24">展望台・タワー</option>
            <option value="25">公園・ビーチ</option>
          </optgroup>
          <optgroup label="Appreciate">
            <option value="26">博物館</option>
            <option value="27">美術館</option>
            <option value="28">資料館</option>
          </optgroup>
          <optgroup label="Shop">
            <option value="29">百貨店</option>
            <option value="30">ファッション</option>
            <option value="31">食品(持ち帰り)</option>
            <option value="32">菓子(持ち帰り)</option>
            <option value="33">酒類(持ち帰り)</option>
            <option value="34">雑貨・土産物</option>
            <option value="35">食器・壷</option>
            <option value="36">宝飾品</option>
            <option value="37">書店</option>
            <option value="38">家電量販店</option>
            <option value="39">スポーツ用品店</option>
            <option value="40">家具屋</option>
            <option value="41">趣味品</option>
          </optgroup>
        </select>
        <br>
        <br>
        <select id="rate%s" name="rate%s" style="width:150px;">
          <option value="">評価を選択</option>
          <option value="1">満足</option>
          <option value="-1">不満</option>
        </select>
        <br>
        <br>
      </div>
    </div>
    """ % (x,x,x,x,x,x,x,x)

  print """
        </div>
      </div>
      <div class="panel-footer">
        <button type="button" class="btn btn-primary btn-small" id="addplace"><i class="glyphicon glyphicon-plus"></i> 訪れた場所を追加</button>
        <button type="button" class="btn btn-default btn-small" id="removeplace"><i class="glyphicon glyphicon-minus"></i> 訪れた場所を減らす</button>
      </div>
    </div>
  </div>
  """

  print """
        <div class="col-md-2 well">
          <div class="col-md-12">
            <div class="row">
              <input type="text" id="userId" name="userId" placeholder="ユーザーIDを入力" style="width:150px;">
            </div>
            <div class="row">
              <input type="date" id="date" name="date" style="width:150px;">
            </div>
            <div class="row">
              <br>
              同伴者を選択:<br>
              <input type="radio" name="companion" value="0"> 一人 <br>
              <input type="radio" name="companion" value="1"> 同性の友人 <br>
              <input type="radio" name="companion" value="2"> 異性の友人 <br>
              <input type="radio" name="companion" value="3"> 親・家族 <br>
            </div>
            <div class="row">
              <br>
              <select id="budget" name="budget">
                <option value="">予算を選択して下さい</option>
                <option value="1">0 ~ 1000円</option>
                <option value="2">1000 ~ 5000円</option>
                <option value="3">5000 ~ 10000円</option>
                <option value="4">10000円以上</option>
              </select>
            </div>
            <br>
            <div class="row">
              <button type="button" class="btn btn-primary" id="submitHistory" style="width:150px;">登録</button>
              <button type="reset" class="btn btn-default" id="resetContext" style="width:150px;">リセット</button>
              <div id="response"></div>
            </div>
          </div>
        </div>
      </div>
    </form>
  </div>

  <!-- Bootstrap core JavaScript
  ================================================== -->
  <!-- Placed at the end of the document so the pages load faster -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  <script src="../dist/js/bootstrap.min.js"></script>
  <script src="../assets/js/docs.min.js"></script>
  <script src="../js/ajax.js"></script>
  <script src="../js/ConnectedSelect.js"></script>
  """
  print "<script>"

  for x in xrange(1,6):
    print "ConnectedSelect(['action%s','genre%s']);" % (x, x)
  print "</script>"
  print "</body></html>"
  import cgitb
  cgitb.enable()


if __name__ == '__main__':
  main()
