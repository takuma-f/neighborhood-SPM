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
                            <li><a href="./cgi_home.py">プラン作成</a></li>
                            <li class='active'><a href="#">情報を登録する</a></li>
                            <li><a href="./cgi_search.py">施設情報を検索</a></li>
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
    """
    print """
            <div class="container">

                <div class="starter-template">
                    <h1>系列の履歴を登録する</h1>
                    <p class="lead">それぞれのユーザーのDBにその時のコンテキストと場所名／ジャンル／行動を記録。</p>
                </div>
                <form method="post" action="./cgi-bin/add_data.cgi">
                <div class="container">
                    <div class="row">
                        <div class="col-md-2">
                            日付 : <input type="date" name="date">
                        </div>
                        <div class="col-md-6">
                            <br>
                            同伴者を選択して下さい : 
                            <input type="radio" name="companion" value="0" checked="checked"> 一人
                            <input type="radio" name="companion" value="1"> 同性の友人
                            <input type="radio" name="companion" value="2"> 異性の友人
                            <input type="radio" name="companion" value="3"> 親・家族
                        </div>
                        <div class="col-md-4">
                            <br>
                            予算を選択して下さい : 
                            <select name="budget">
                                <option value="0">0 ~ 1000円</option>
                                <option value="1">1000 ~ 5000円</option>
                                <option value="2">5000 ~ 10000円</option>
                                <option value="3">10000円以上</option>
                            </select>
                        </div>
                    </div>
                    <br>
    """
    print """
                    <div class="row">
                        <div class="col-md-2">
                            場所の名前を入力 :
                        </div>
    """

    for x in xrange(1,6):
        print """
                        <div class="col-md-2">
                            <input type="text" name="venue%s"/>
                        </div>
        """ % x

    print """
                    </div>
                    <br>
                    <div class="row">
                        <div class="col-md-2">
                            取った行動を選択 :
                        </div>
    """

    for x in xrange(1,6):
        print """
                        <div class="col-md-2">
                            <select name="action%s">
                                <option value="Eat">食事する</option>
                                <option value="Tea">お茶する</option>
                                <option value="Bar">居酒屋・バーで飲む</option>
                                <option value="Shop">買い物する</option>
                                <option value="Play">遊ぶ</option>
                            </select>
                        </div>
        """ % x

    print """
                    </div>
                    <br>
                    <div class="row">
                        <div class="col-md-4">
                            <input type="submit" value="登録">
                            <input type="reset" value="リセット">
                        </div>
                    </div>
                </div>
                </form>
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
