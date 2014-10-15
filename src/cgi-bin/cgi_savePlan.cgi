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
        f.write(form['userId'].value + ","\
        + form['date'].value + ","\
        + form['companion'].value + ","\
        + form['budget'].value + ","\
        + form['order'].value + ","\
        + form['amount'].value + ","\
        + form['which'].value + ",\r\n"\
        + "seed," + form['seed'].value + ",\r\n"\
        + form['data_iter'].value + ",\r\n"\
        + form['sim_iter'].value + ",\r\n"\
        + form['type1'].value + ","\
        + form['amount1'].value + ","\
        + form['score1'].value + ","\
        + form['pattern1'].value + ",\r\n"\
        + form['type2'].value + ","\
        + form['amount2'].value + ","\
        + form['score2'].value + ","\
        + form['pattern2'].value + ",\r\n"\
        + form['type3'].value + ","\
        + form['amount3'].value + ","\
        + form['score3'].value + ","\
        + form['pattern3'].value + ",\r\n"\
        + form['type4'].value + ","\
        + form['amount4'].value + ","\
        + form['score4'].value + ","\
        + form['pattern4'].value + ",\r\n"\
        + form['type5'].value + ","\
        + form['amount5'].value + ","\
        + form['score5'].value + ","\
        + form['pattern5'].value + ",\r\n"\
        + form['type6'].value + ","\
        + form['amount6'].value + ","\
        + form['score6'].value + ","\
        + form['pattern6'].value + ",\r\n"\
        + form['venue1'].value + ","\
        + form['venue2'].value + ","\
        + form['venue3'].value + ","\
        + form['venue4'].value + ","\
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
