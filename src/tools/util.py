#!/usr/bin/env python
# coding: UTF-8

import sys
import traceback

def printError():
    # エラー出力用のメソッド(util.pyに移動？)
    info = sys.exc_info()  # エラーの情報をsysモジュールから取得
    tbinfo = traceback.format_tb(info[2])  # tracebackモジュールのformat_tbメソッドで特定の書式に変換
    for tb in tbinfo:
        print tb
    print "%s" % str(info[1])
    print