#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib2

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class fanyi_dictionary(object):
    def __init__(self, word):
        self.word_quote = urllib2.quote(word)
        filename = os.getenv("HOME") + "/.ldict/fanyi/" + self.word_quote + ".xml"

        global root
        if len(self.word_quote) > 255:
            xml = urllib2.urlopen("http://fanyi.youdao.com/openapi.do?keyfrom=Lindict&key=1841534375&type=data&doctype=xml&version=1.1&q="
                                  + self.word_quote, timeout = 1).read()
            root = ET.fromstring(xml)
        else:
            if os.path.exists(filename) != True:
                xml = urllib2.urlopen("http://fanyi.youdao.com/openapi.do?keyfrom=Lindict&key=1841534375&type=data&doctype=xml&version=1.1&q="
                                      + self.word_quote, timeout = 1).read()
                f = open(filename, 'w')
                f.write(xml)
                f.close()
            tree = ET.ElementTree(file=filename)
            root = tree.getroot()
        
        self.errorCode = ""
        self.query = ""
        self.translation = ""
        self.basic = []
        self.phonetic = ""
        self.explains = []
        self.web = []

        self.unpack_root(root)
        self.unpack_basic()
        
    def unpack_root(self, root):
        for element in root:
            if element.tag == "errorCode":
                self.errorCode = element.text
            elif element.tag == "query":
                self.query = element.text
            elif element.tag == "translation":
                self.translation = element[0].text
            elif element.tag == "basic":
                self.basic = element
            elif element.tag == "web":
                for child in element:
                    self.web.append(child)
                    
    def unpack_basic(self):
        for element in self.basic:
            if element.tag == "phonetic":
                self.phonetic = element.text
            elif element.tag == "explains":
                for child in element:
                    self.explains.append(child.text)

    def web_explains(self):
        web_explains = {}
        for element in self.web:
            key = ""
            value = []
            for child in element:
                if child.tag == "value":
                    for ex in child:
                        value.append(ex.text)
                elif child.tag == "key":
                   key = child.text
            web_explains[key] = value
        return web_explains
                    
