#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
import cgi
import cgitb
import random
import time

from apriori import genPattern as apriori
from tools import util as util


def main():
    unixtime = int(time.time())
    random.seed(unixtime)  # 乱数シードを設定(POPとrandam)
    input_data = cgi.FieldStorage()
    genre1 = input_data["genre1"].value
    genre2 = input_data["genre2"].value
    genre3 = input_data["genre3"].value
    genre4 = input_data["genre4"].value
    genre5 = input_data["genre5"].value
    genre_set = [genre1, genre2, genre3, genre4, genre5]
    rand_p1 = apriori.genRandomPattern(genre_set, 5, 10)
    rand_p2 = apriori.genRandomPattern(genre_set, 4, 10)
    rand_p3 = apriori.genRandomPattern(genre_set, 3, 10)
    print "<!DOCTYPE html>"

    for x, p in enumerate(xrange(1, 11)):
        counter = x + 1
        print """
<div id="panel%s" class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">行動パターン%s</h3>
  </div>
  <div class="panel-body">
    <div class="row">
      <form id="patternForm">
        <div class="col-md-1"></div>
        """ % (counter, counter)

        # if counter < 6:
        #     p = rand_p1.pop()
        # elif 5 < counter < 9:
        #     p = rand_p2.pop()
        # elif 8 < counter < 11:
        #     p = rand_p3.pop()
        if counter < 11:
            p = rand_p1.pop()
        convert_p = util.convertAction(p)
        for o, item in enumerate(convert_p):
            print"""
            <div class="col-md-2" id="ItemBox">
              %s箇所目：%s
            </div>
            """ % (o+1, item)
        print '<input type="hidden" id="pattern%s" value="%s">' % (counter ,p)

        print """
        </form>
      </div>
    </div>
    <div class="panel-footer">
        """

        print"""
      <input type="radio" form="patternForm" name="rate%s" value="1"> このプランは好き！
      <input type="radio" form="patternForm" name="rate%s" value="-1"> このプランは嫌い
        """ % (counter, counter)

        if counter == 10:
            print"""
      <br />
      <br />
      <button type="button" class="btn btn-primary btn-small" id="saveRating" form="patternForm" value="%s">
        <i class="glyphicon glyphicon-plus"></i> 評価を送信！
      </button>
      <span id="response"></span>
            """ % (counter)

        print"""
  </div>
</div>
        """
    print """
<script src="../js/ajax2.js"></script>
    """
    cgitb.enable()


if __name__ == '__main__':
    main()
