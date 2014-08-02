#!/usr/bin/env python
# coding: UTF-8

import sys
import traceback


def printError():
    # エラー出力用のメソッド
    # エラーの情報をsysモジュールから取得
    info = sys.exc_info()
    # tracebackモジュールのformat_tbメソッドで特定の書式に変換
    tbinfo = traceback.format_tb(info[2])
    print "="*50
    for tb in tbinfo:
        print tb
    print "%s" % str(info[1])
    print "="*50


def convertAction(pattern):
    # 出力時に日本語に直す
    convertedSet = list()

    for action in pattern:
        if action == "Eat":
            convertedSet.append("食事する")
        elif action == "Tea":
            convertedSet.append("お茶する")
        elif action == "Play":
            convertedSet.append("遊ぶ")
        elif action == "Sight":
            convertedSet.append("名所・名勝を見る")
        elif action == "Appreciate":
            convertedSet.append("鑑賞する")
        elif action == "Shop":
            convertedSet.append("買い物する")
    return convertedSet
