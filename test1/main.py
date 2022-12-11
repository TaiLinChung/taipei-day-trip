#
# @file main.py
#

import arithmetic as a4

def letscook(x, y, oper):
    r = 0
    if oper == "+":
        r = a4.add(x, y)
    elif oper == "-":
        r = a4.sub(x, y)
    elif oper == "*":
        r = a4.mul(x, y)
    else:
        r = a4.dev(x, y)

    aa=("{} {} {} = {}".format(x, oper, y, r))
    print("輸出: ",aa)

x, y = 3, 8

letscook(x, y, "+")
letscook(x, y, "-")
letscook(x, y, "*")
letscook(x, y, "/")