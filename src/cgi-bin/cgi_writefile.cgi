#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
import cgi
import cgitb
from tools import util as util


# 履歴情報をファイルに追記・保存する
def writeFile(form):
    f = None
    try:
        f = open('userData/'+form['userId'].value+'_history.txt', 'a')
        f.write(form['date'].value + \
            ", " + form['companion'].value + \
            ", " + form['budget'].value + \
            ", " + form['venue1'].value + \
            ", " + form['venue2'].value + \
            ", " + form['venue3'].value + \
            ", " + form['venue4'].value + \
            ", " + form['venue5'].value + \
            ", " + form['genre1'].value + \
            ", " + form['genre2'].value + \
            ", " + form['genre3'].value + \
            ", " + form['genre4'].value + \
            ", " + form['genre5'].value + \
            ", " + form['action1'].value + \
            ", " + form['action2'].value + \
            ", " + form['action3'].value + \
            ", " + form['action4'].value + \
            ", " + form['action5'].value + \
            ", " + form['rate1'].value + \
            ", " + form['rate2'].value + \
            ", " + form['rate3'].value + \
            ", " + form['rate4'].value + \
            ", " + form['rate5'].value + \
            "\r\n")
    except IOError:
        util.printError()
    finally:
        if(f):
            f.close()


def main():
    print "<!DOCTYPE html>"
    form = cgi.FieldStorage()
    print form
    writeFile(form)
    cgitb.enable()


if __name__ == '__main__':
    main()
