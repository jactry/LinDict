#! /usr/bin/python
# -*- coding: utf-8 -*-
import re
import urllib
import urllib2
import sys
import os
from en_engine import en_dictionary
from fanyi_engine import fanyi_dictionary

def look_up(word):
    mydictionary = en_dictionary(str(word))
    myfanyi = fanyi_dictionary(str(word))
    res = translate(mydictionary, myfanyi)
    return res

def translate(mydictionary, myfanyi):
    res = u"<div style=\"font-family:Ubuntu\"><center><p><span style=\"font-size:25px; font-weight:bold; color:#000;\">" + str(mydictionary.return_phrase) + "</span>"
    if mydictionary.phonetic_symbol:
        res+="<span style=\"font-size:15px; color:#0000b1;\">   ["+ str(mydictionary.phonetic_symbol) +"]</span>"
    res += "</p></center>"

    if mydictionary.cn_translation:
        res += "<ul>"
        for trans in mydictionary.cn_translation:
            res += "<li>" + str(trans) + "</li>"
        res += "</ul>"

    word_forms = mydictionary.word_forms()
    if word_forms:
        res += "变形：<ul>"
        for x in word_forms.keys():    
            res += "<li>" + str(x) + ": " + word_forms[x] + "</li>"
        res += "</ul>"

    web_explains = myfanyi.web_explains()
    if web_explains:
        res += "词组：<ul>"
        for explain in web_explains.keys():
            res += "<li>" + explain + ": "
            for value in web_explains[explain]:
                res += value
            res += "</li>"
        res += "</ul>"
 
    example_sentences = mydictionary.example_sentence()
    if example_sentences:
        res += "例句：<ul>"
        for x in example_sentences.keys():
            res += "<li>" + str(x) + "<br>" + str(example_sentences[x]) + "</li>"
        res += "</ul>"
    return res
