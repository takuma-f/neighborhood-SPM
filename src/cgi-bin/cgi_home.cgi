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
      <a class="navbar-brand" href="#">Perfect Planner</a>
      </div>
      <div class="collapse navbar-collapse">
        <ul class="nav navbar-nav">
          <li class="active"><a href=""><i class="glyphicon glyphicon-home"></i> プラン作成</a></li>
          <li><a href="./cgi_add.cgi"><i class="glyphicon glyphicon-plus-sign"></i> 情報を登録する</a></li>
          <li><a href="./cgi_viewplan.cgi"><i class="glyphicon glyphicon-list"></i> 保存したプランを見る</a></li>
          <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">その他<span class="caret"></span></a>
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
    <br>
    <div class="row">
      <div id="planArea" class="col-md-10"></div>
      <div class="col-md-2 well">
        <div class="col-md-12">
          <form action="#">
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
          </form>
          <br>
          <div class="row">
            <button type="button" class="btn btn-primary" id="submitContext" style="width:150px;">プランを作る</button>
            <button type="reset" class="btn btn-default" id="resetContext" style="width:150px;">条件をリセット</button>
          </div>
        </div>
      </div>
    </div>
  </div>
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="../js/jquery-1.11.1.min.js"></script>
    <script src="../dist/js/bootstrap.min.js"></script>
    <script src="../assets/js/docs.min.js"></script>
    <script src="../js/ajax.js"></script>
  """
  print "</body></html>"
  import cgitb
  cgitb.enable()


if __name__ == '__main__':
  main()
