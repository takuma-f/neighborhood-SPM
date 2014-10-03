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
        f = open('userData/'+form['userId'].value+'.log', 'a')
        f.write(form['userId'].value + ", "\
        + form['date'].value + ", "\
        + form['companion'].value + ", "\
        + form['budget'].value + ", "\
        + form['order'].value + ", "\
        + form['amount'].value + ", "\
        + form['which'].value + ", \r\n"\
        + form['pattern1'].value + ", \r\n"\
        + form['pattern2'].value + ", \r\n"\
        + form['pattern3'].value + ", \r\n"\
        + form['pattern4'].value + ", \r\n"\
        + form['pattern5'].value + ", \r\n"\
        + form['pattern6'].value + ", \r\n"\
        + form['venue1'].value + ", "\
        + form['venue2'].value + ", "\
        + form['venue3'].value + ", "\
        + form['venue4'].value + ", "\
        + form['venue5'].value + "\r\n\r\n")
    except Exception:
        raise
    finally:
        if(f):
            f.close()


def main():
    print '<!DOCTYPE html>'
    try:
        form = cgi.FieldStorage()
        writeFile(form)
    except Exception:
        raise
    cgitb.enable()


if __name__ == '__main__':
    main()
