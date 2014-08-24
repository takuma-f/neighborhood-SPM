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
        f = open('userData/'+form['userId'].value+'_saved.txt', 'a')
        f.write(form['date'].value + ", "\
        + form['userId'].value + ", "\
        + form['companion'].value + ", "\
        + form['budget'].value + ", "\
        + form['venue1'].value + ", "\
        + form['venue2'].value + ", "\
        + form['venue3'].value + ", "\
        + form['venue4'].value + ", "\
        + form['venue5'].value + ", "\
        + form['order'].value + "\r\n")
    except IOError:
        util.printError()
    finally:
        if(f):
            f.close()


def main():
    print '<!DOCTYPE html>'
    form = cgi.FieldStorage()
    writeFile(form)
    cgitb.enable()


if __name__ == '__main__':
    main()
