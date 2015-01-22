#!/usr/bin/env python
# coding: UTF-8

import sys
sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
sys.stderr = sys.stdout
import cgi
import cgitb
from tools import util as util
from copy import deepcopy


# 履歴情報をファイルに追記・保存する
def writeFile(form):
    action_list = list()
    genre_list = list()
    count = 0
    f = None
    try:
        f = open('userData/'+form['userId'].value+'_history.txt', 'a')

        for i in xrange(1, 11):
            pattern = form['pattern'+str(i)].value

            pattern = util.convertList(pattern)
            pattern2 = deepcopy(pattern)
            pattern2 = util.arrangeGenreList(pattern2)
            genre_list.append(pattern2)

            actions = util.detParentAction(pattern)
            actions = util.arrangeActionList(actions)
            action_list.append(actions)

        for genres, actions in zip(genre_list, action_list):
            count += 1
            f.write(form['date'].value + \
                ", " + form['companion'].value + \
                ", " + form['budget'].value + ", ")
            for action in actions:
                f.write(str(action) + ", ")
            for genre in genres:
                f.write(str(genre) + ", ")
            for action in actions:
                f.write(str(action) + ", ")
            f.write(form['rate'+str(count)].value + "\r\n")
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
        reise
    cgitb.enable()


if __name__ == '__main__':
    main()
