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
        f.write("date: " + form['date'].value + "\r\n"\
        + "companion: " + form['companion'].value + "\r\n"\
        + "budget: " + form['budget'].value + "\r\n"\
        + "seed: " + form['seed'].value + "\r\n"\
        + "type: "\
        + form['type1'].value + ","\
        + form['type2'].value + ","\
        + form['type3'].value + ","\
        + form['type4'].value + ","\
        + form['type5'].value + ","\
        + form['type6'].value + "\r\n"\
        + "rate: "\
        + form['rate1'].value + ","\
        + form['rate2'].value + ","\
        + form['rate3'].value + ","\
        + form['rate4'].value + ","\
        + form['rate5'].value + ","\
        + form['rate6'].value + "\r\n"\
        + "amount: "\
        + form['amount1'].value + ","\
        + form['amount2'].value + ","\
        + form['amount3'].value + ","\
        + form['amount4'].value + ","\
        + form['amount5'].value + ","\
        + form['amount6'].value + "\r\n"\
        + "score: "\
        + form['score1'].value + ","\
        + form['score2'].value + ","\
        + form['score3'].value + ","\
        + form['score4'].value + ","\
        + form['score5'].value + ","\
        + form['score6'].value + "\r\n"\
        + form['pattern1'].value + ",\r\n"\
        + form['pattern2'].value + ",\r\n"\
        + form['pattern3'].value + ",\r\n"\
        + form['pattern4'].value + ",\r\n"\
        + form['pattern5'].value + ",\r\n"\
        + form['pattern6'].value + ",\r\n\r\n")
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
