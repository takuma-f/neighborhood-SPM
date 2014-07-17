#!/usr/bin/env python
# coding: UTF-8


def test_cgi():
    print "Content-type: text/html"
    print
    print "<html><head><title>Neighborhood</title></head><body><pre>"
    import sys
    sys.path.append('/Users/Admin/dev/neighborhood_SPM/src/')
    sys.stderr = sys.stdout

    from neighborhood import neighborhood as neigh
    import os
    from cgi import escape

    transaction_list = [['Eat', 'Bar'], ['Eat', 'Tea', 'Shop', 'Eat', 'Play'], ['Eat', 'Tea', 'Shop', 'Eat', 'Bar'], ['Eat', 'Bar'], ['Shop', 'Eat', 'Play'], ['Play', 'Bar'], ['Eat', 'Bar'], ['Eat', 'Shop', 'Eat', 'Play', 'Bar']]

    patterns = [['Eat'], ['Bar'], ['Eat', 'Bar'], ['Tea'], ['Shop'], ['Play'], ['Eat', 'Tea'], ['Eat', 'Shop'], ['Eat', 'Eat'], ['Eat', 'Play'], ['Tea', 'Shop'], ['Tea', 'Eat'], ['Tea', 'Play'], ['Shop', 'Eat'], ['Shop', 'Play'], ['Eat', 'Tea', 'Shop'], ['Eat', 'Tea', 'Eat'], ['Eat', 'Tea', 'Play'], ['Eat', 'Shop', 'Eat'], ['Eat', 'Shop', 'Play'], ['Eat', 'Eat', 'Play'], ['Tea', 'Shop', 'Eat'], ['Tea', 'Shop', 'Play'], ['Tea', 'Eat', 'Play'], ['Shop', 'Eat', 'Play'], ['Eat', 'Tea', 'Shop', 'Eat'], ['Eat', 'Tea', 'Shop', 'Play'], ['Eat', 'Tea', 'Eat', 'Play'], ['Eat', 'Shop', 'Eat', 'Play'], ['Tea', 'Shop', 'Eat', 'Play'], ['Eat', 'Tea', 'Shop', 'Eat', 'Play'], ['Tea', 'Bar'], ['Shop', 'Bar'], ['Eat', 'Tea', 'Bar'], ['Eat', 'Shop', 'Bar'], ['Eat', 'Eat', 'Bar'], ['Tea', 'Shop', 'Bar'], ['Tea', 'Eat', 'Bar'], ['Shop', 'Eat', 'Bar'], ['Eat', 'Tea', 'Shop', 'Bar'], ['Eat', 'Tea', 'Eat', 'Bar'], ['Eat', 'Shop', 'Eat', 'Bar'], ['Tea', 'Shop', 'Eat', 'Bar'], ['Eat', 'Tea', 'Shop', 'Eat', 'Bar'], ['Play', 'Bar'], ['Eat', 'Play', 'Bar'], ['Shop', 'Play', 'Bar'], ['Eat', 'Shop', 'Play', 'Bar'], ['Eat', 'Eat', 'Play', 'Bar'], ['Shop', 'Eat', 'Play', 'Bar'], ['Eat', 'Shop', 'Eat', 'Play', 'Bar']]

    pattern_dict = neigh.getSortedDict(transaction_list, patterns)
    count = 0
    for key, value in pattern_dict:
        print value
        count += 1
        if count == 3:  # 上位3個だけ出力
            break

    print "</pre></body></html>"

    import cgitb
    cgitb.enable()

if __name__ == '__main__':
    test_cgi()
