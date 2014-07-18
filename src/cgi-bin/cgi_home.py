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

    transaction_list = [['Eat', 'Bar'], ['Eat', 'Tea', 'Shop', 'Eat', 'Play'], ['Eat', 'Tea', 'Shop', 'Eat', 'Bar'], ['Eat', 'Bar'], ['Shop', 'Eat', 'Play'], ['Play', 'Bar'], ['Eat', 'Bar'], ['Eat', 'Shop', 'Eat', 'Play', 'Bar']]

    patterns = [['Eat'], ['Bar'], ['Eat', 'Bar'], ['Tea'], ['Shop'], ['Play'], ['Eat', 'Tea'], ['Eat', 'Shop'], ['Eat', 'Eat'], ['Eat', 'Play'], ['Tea', 'Shop'], ['Tea', 'Eat'], ['Tea', 'Play'], ['Shop', 'Eat'], ['Shop', 'Play'], ['Eat', 'Tea', 'Shop'], ['Eat', 'Tea', 'Eat'], ['Eat', 'Tea', 'Play'], ['Eat', 'Shop', 'Eat'], ['Eat', 'Shop', 'Play'], ['Eat', 'Eat', 'Play'], ['Tea', 'Shop', 'Eat'], ['Tea', 'Shop', 'Play'], ['Tea', 'Eat', 'Play'], ['Shop', 'Eat', 'Play'], ['Eat', 'Tea', 'Shop', 'Eat'], ['Eat', 'Tea', 'Shop', 'Play'], ['Eat', 'Tea', 'Eat', 'Play'], ['Eat', 'Shop', 'Eat', 'Play'], ['Tea', 'Shop', 'Eat', 'Play'], ['Eat', 'Tea', 'Shop', 'Eat', 'Play'], ['Tea', 'Bar'], ['Shop', 'Bar'], ['Eat', 'Tea', 'Bar'], ['Eat', 'Shop', 'Bar'], ['Eat', 'Eat', 'Bar'], ['Tea', 'Shop', 'Bar'], ['Tea', 'Eat', 'Bar'], ['Shop', 'Eat', 'Bar'], ['Eat', 'Tea', 'Shop', 'Bar'], ['Eat', 'Tea', 'Eat', 'Bar'], ['Eat', 'Shop', 'Eat', 'Bar'], ['Tea', 'Shop', 'Eat', 'Bar'], ['Eat', 'Tea', 'Shop', 'Eat', 'Bar'], ['Play', 'Bar'], ['Eat', 'Play', 'Bar'], ['Shop', 'Play', 'Bar'], ['Eat', 'Shop', 'Play', 'Bar'], ['Eat', 'Eat', 'Play', 'Bar'], ['Shop', 'Eat', 'Play', 'Bar'], ['Eat', 'Shop', 'Eat', 'Play', 'Bar']]

    pattern_dict = neigh.getSortedDict(transaction_list, patterns)

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
                            <li class="active"><a href="#">プラン作成</a></li>
                            <li><a href="./cgi_add.py">情報を登録する</a></li>
                            <li><a href="./cgi_search.py">施設情報を検索</a></li>
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
                    <h1>行動プラン推薦画面</h1>
                    <p class="lead">ユーザーが好むと思われる行動プランを表示し、それぞれの行動に場所を当てはめさせる</p>
                </div>

                <div class="col-md-6">
                    <div class="list-group">
                        <a href="#" class="list-group-item">
                            <h4 class="list-group-item-heading">プラン候補1</h4>
                            <p class="list-group-item-text">ここに</p>
                        </a>
                        <a href="#" class="list-group-item">
                            <h4 class="list-group-item-heading">プラン候補2</h4>
                            <p class="list-group-item-text">プログラムで評価値を求めた</p>
                        </a>
                        <a href="#" class="list-group-item">
                            <h4 class="list-group-item-heading">プラン候補3</h4>
                            <p class="list-group-item-text">パターンがはいる</p>
                        </a>
                    </div>
                </div>

                <div class="col-md-6">
                    <div class="list-group">
                        <a href="#" class="list-group-item">
                            <h4 class="list-group-item-heading">アイテム候補1</h4>
                            <p class="list-group-item-text">ここに左で選択したパターンの</p>
                        </a>
                        <a href="#" class="list-group-item">
                            <h4 class="list-group-item-heading">アイテム候補2</h4>
                            <p class="list-group-item-text">各行動に対応した</p>
                        </a>
                        <a href="#" class="list-group-item">
                            <h4 class="list-group-item-heading">アイテム候補3</h4>
                            <p class="list-group-item-text">アイテムが表示される</p>
                        </a>
                    </div>
                </div>

            </div><!-- /.container -->
    """
    print """
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
