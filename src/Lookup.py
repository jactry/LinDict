#! /usr/bin/python
# -*- coding: utf-8 -*-

from en_engine import en_dictionary
from fanyi_engine import fanyi_dictionary


def look_up(word):
    mydictionary = en_dictionary(str(word))
    myfanyi = fanyi_dictionary(str(word))
    res = translate(mydictionary, myfanyi)
    return res


def translate(mydictionary, myfanyi):
    res = """<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <link href="resrc/styles/base.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    """
    res += "<center><h2><div class=\"keyword\">" + str(mydictionary.return_phrase) + "</div></h2>"
    if mydictionary.phonetic_symbol:
        res += "<div class=\"phonetic\"> [" + str(mydictionary.phonetic_symbol) + "] </div>"
    res += "</center>"

    if mydictionary.cn_translation:
        res += "<div class=\"trans-container\"><h4><ul>"
        for trans in mydictionary.cn_translation:
            res += "<li>" + str(trans) + "</li>"
        res += "</ul></h4></div>"

    word_forms = mydictionary.word_forms()
    if word_forms:
        res += "<center><div class=\"additional\">["
        for x in word_forms.keys():
            res += str(x) + ": " + word_forms[x] + " "
        res += "]</div></center>"

    web_explains = myfanyi.web_explains()
    if web_explains:
        res += "<h3>词组：</h3><ul>"
        for explain in web_explains.keys():
            res += "<li><div class=\"contentTitle\">" + explain + ": </div>"
            for value in web_explains[explain]:
                res += value
            res += "</li>"
        res += "</ul>"
    example_sentences = mydictionary.example_sentence()
    if example_sentences:
        res += "<h3>例句：</h3><ol>"
        for x in example_sentences.keys():
            res += "<li>" + str(x) + "<br>" + str(example_sentences[x]) + "</li>"
        res += "</ol></hbody></html>"
    return res
