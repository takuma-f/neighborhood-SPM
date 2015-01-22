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
            <link href="../dist/css/jumbotron.css" rel="stylesheet">

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
                <div class="navbar-collapse collapse">
                  <form class="navbar-form navbar-right" role="form">
                    <div class="form-group">
                      <input type="text" placeholder="Email" class="form-control">
                    </div>
                    <div class="form-group">
                      <input type="password" placeholder="Password" class="form-control">
                    </div>
                    <button type="submit" class="btn btn-success">Sign in</button>
                  </form>
                </div><!--/.navbar-collapse -->
              </div>
            </div>

            <!-- Main jumbotron for a primary marketing message or call to action -->
            <div class="jumbotron">
                <div class="container">
                    <h1>The Plan <br> is <br> inside of you.</h1>
                    <p>Perfect Plannerはあなたの行動パターンを記録し、見知らぬ土地でもあなたにぴったりの行動プランをサジェスト <br> してくれます。これによってあなたは本当に行くべき場所を選ぶことに集中することができるのです。</p>
                    <p><a class="btn btn-primary btn-lg" role="button">Sign up &raquo;</a></p>
                </div>
            </div>


            <div class="container">
                <!-- Example row of columns -->
                <div class="row">
                    <div class="col-md-4">
                        <h2>プランを作成する</h2>
                        <p>さあ出かけましょう。<br>
                        Perfect Plannerはあなたがいつ何をしたいか全て知っています。</p>
                    </div>
                    <div class="col-md-4">
                        <h2>新しい履歴を登録する</h2>
                        <p>昨日はどんな所へ行きましたか？<br>
                        Perfect Plannerはあなたの行動を学習し、よりあなたに合ったプランを考えます。</p>
                    </div>
                    <div class="col-md-4">
                        <h2>施設情報を検索する</h2>
                        <p>ご自身で開拓されますか？<br>
                        Perfect Plannerのデータベースを検索し、新たな発見をしましょう。</p>
                    </div>
                </div>

                <hr>

                <footer>
                    <p>&copy; Takuma FUJITSUKA 2014</p>
                </footer>
            </div> <!-- /container -->


            <!-- Bootstrap core JavaScript
            ================================================== -->
            <!-- Placed at the end of the document so the pages load faster -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
            <script src="../../dist/js/bootstrap.min.js"></script>
    """
    print "</body></html>"
    import cgitb
    cgitb.enable()


if __name__ == '__main__':
    main()
