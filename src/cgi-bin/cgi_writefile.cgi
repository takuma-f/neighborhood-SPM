#!/usr/bin/env python
# coding: UTF-8


def main():
  print "<!DOCTYPE html>"
  print
  print """
  <html lang="ja">
    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="description" content="素晴らしくNice choice.な">
      <meta name="TakumaFUJITSUKA" content="">
      <link rel="icon" href="../../favicon.ico">

      <title>Perfect Planner</title>
    </head>
  """


  import sys
  sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
  sys.stderr = sys.stdout
  import cgi

  form = cgi.FieldStorage()

  #ファイル書込処理
  file = None
  try:
    file = open("./test.txt", "a")
    file.write(form["date"].value + \
      ", companion:" + form["companion"].value + \
      ", budget:" + form["budget"].value + \
      ", venue1:" + form["venue1"].value + \
      ", venue2:" + form["venue2"].value + \
      ", venue3:" + form["venue3"].value + \
      ", venue4:" + form["venue4"].value + \
      ", venue5:" + form["venue5"].value + \
      # ", genre1:" + form["genre1"].value + \
      # ", genre2:" + form["genre2"].value + \
      # ", genre3:" + form["genre3"].value + \
      # ", genre4:" + form["genre4"].value + \
      # ", genre5:" + form["genre5"].value + \
      # ", action1:" + form["action1"].value + \
      # ", action2:" + form["action2"].value + \
      # ", action3:" + form["action3"].value + \
      # ", action4:" + form["action4"].value + \
      # ", action5:" + form["action5"].value + \
      "\r\n")
    print "Location: ./cgi_add.py\n\n"
  except IOError:
    print "Location: ./cgi_add.py\n\n"
  finally:
    if(file):
      file.close()

  print "</body></html>"
  import cgitb
  cgitb.enable()

if __name__ == '__main__':
  main()

# form["venue1"].value + form["venue2"].value + form["venue3"].value + form["venue4"].value + form["venue5"].value + form["genre1"].value + form["genre2"].value + form["genre3"].value + form["genre4"].value + form["genre5"].value + form["action1"].value + form["action2"].value + form["action3"].value + form["action4"].value + form["action5"].value + 