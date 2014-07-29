#!/usr/bin/env python
# coding: UTF-8


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
    </head>

    <body>
  """

  import sys
  sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
  sys.stderr = sys.stdout
  import os
  from cgi import escape
  from neighborhood import neighborhood as neigh
  from apriori import genPattern as apriori
  from apriori import genIter as genIter

  print """
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
              <li class="active"><a href="">プラン作成</a></li>
              <li><a href="./cgi_add.cgi">情報を登録する</a></li>
              <li><a href="./cgi_search.cgi">施設情報を検索</a></li>
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
        <div class="starter-template">
          <h1>プランを作成</h1>
          <p class="lead">今度の休日は誰とどこへ行きますか？Perfect Plannerがお手伝いします</p>
        </div>
        <form method="post" action="./cgi_inputContext.cgi">
          <div class="row">
            <div class="col-md-2">
              ユーザーID : <input type="text" name="userId" placeholder="ユーザーIDを入力">
            </div>
          </div>
          <div class="row">
            <div class="col-md-2">
              日付 : <input type="date" name="date">
            </div>
            <div class="col-md-6">
              <br>
              同伴者を選択して下さい : 
              <input type="radio" name="companion" value="0"> 一人
              <input type="radio" name="companion" value="1"> 同性の友人
              <input type="radio" name="companion" value="2"> 異性の友人
              <input type="radio" name="companion" value="3"> 親・家族
            </div>
            <div class="col-md-4">
              <br>
              予算を選択して下さい : 
              <select name="budget">
                <option value="0"></option>
                <option value="1">0 ~ 1000円</option>
                <option value="2">1000 ~ 5000円</option>
                <option value="3">5000 ~ 10000円</option>
                <option value="4">10000円以上</option>
              </select>
            </div>
          </div>
          <br>
          <div class="row">
            <div class="col-md-4">
              <input type="submit" value="条件を変更">
              <input type="reset" value="リセット">
            </div>
          </div>
        </form>
  """

  # print '<div class="col-md-10">'
  # count = 0
  # for key, value in pattern_dict:
  #   count += 1
  #   value = neigh.convertAction(value)

  #   print """
  #         <div class="list-group">
  #           <div class="list-group-item">
  #             <h4 class="list-group-item-heading">プラン候補%s</h4>
  #             <p class="list-group-item-text">
  #   """ % count
  #   print '<div class="row">'
  #   for action in value:
  #     print '<div class="col-md-2">'
  #     print action
  #     print '</div>'
  #   print '</div>'
  #   print '<div class="row">'
  #   for action in value:
  #     print '<div class="col-md-2">'
  #     print """
  #               <select name="action%s" size="5">
  #                 <option value="1">食神餃子王</option>
  #                 <option value="2">サンマルクカフェ</option>
  #                 <option value="3">厨ぼうず</option>
  #                 <option value="4">ラーメンそらまめ</option>
  #                 <option value="5">インド料理Raja</option>
  #                 <option value="6">調布パルコ</option>
  #                 <option value="7">深大寺</option>
  #                 <option value="8">神代植物公園</option>
  #                 <option value="9">調布飛行場</option>
  #                 <option value="10">電気通信大学</option>
  #               </select>
  #     """ % count
  #     print '</div>'
  #   print '</div>'
  #   print """
  #             </p>
  #           </div>
  #         </div>
  #   """
  #   if count == 5:  # 上位5個だけ出力
  #     # break
  # print "</div>"

  print """
      </div><!-- /.container -->
      <!-- Bootstrap core JavaScript
      ================================================== -->
      <!-- Placed at the end of the document so the pages load faster -->
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
      <script src="../dist/js/bootstrap.min.js"></script>
      <script src="../assets/js/docs.min.js"></script>
  """
  print "</body></html>"
  import cgitb
  cgitb.enable()


if __name__ == '__main__':
  main()
