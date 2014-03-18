#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def build():
    os.system("pyuic4 -o ui_main.py ./ui/ui_main.ui")
    print "pyuic4 -o ui_main.py ./ui/ui_main.ui"
    os.system("pyuic4 -o ui_close.py ./ui/ui_close.ui")
    print "pyuic4 -o ui_close.py ./ui/ui_close.ui"
    os.system("pyrcc4 -o youdao_rc.py youdao.qrc")
    print "pyrcc4 -o youdao_rc.py youdao.qrc"

if __name__ == "__main__":

    build()
