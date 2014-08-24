#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
import cgi
import cgitb


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
        print '<span id="alert">登録完了.</span>'
    except Exception:
        print '<span id="alert">入力エラー.</span>'
    cgitb.enable()


if __name__ == '__main__':
    main()
