#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib2

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class en_dictionary(object):
    def __init__(self, word):
        self.word_quote = urllib2.quote(word)
        filename = os.getenv("HOME") + "/.ldict/dict/" + self.word_quote + ".xml"
        if os.path.exists(filename) != True:
            xml = urllib2.urlopen("http://dict.youdao.com/search?le=eng&q="+ self.word_quote
                                  +"&xmlDetail=true&doctype=xml", timeout = 1).read()
            f = open(filename, 'w')
            f.write(xml)
            f.close()
        tree = ET.ElementTree(file=filename)
        root = tree.getroot()

        self.original_query = ""
        self.return_phrase = ""
        self.phonetic_symbol = ""
        self.custom_translation = []
        self.cn_translation = []
        self.all_word_forms = []
        self.dictcn_speach = []
        self.example_sentences = []
        self.yodao_link = ""
        self.speak_link = "http://dict.youdao.com/dictvoice?audio=" + self.word_quote
        
        self.unpack_root(root)
        self.unpack_cn_custom_translation()
        
    def unpack_root(self, root):
        for element in root:
            if element.tag == "original-query":
                self.original_query = element.text
            elif element.tag == "return-phrase":
                self.return_phrase = element.text
            elif element.tag == "phonetic-symbol":
                self.phonetic_symbol = element.text
            elif element.tag == "custom-translation":
                self.custom_translation.append(element)
            elif element.tag == "yodao-link":
                self.yodao_link = element.text
            elif element.tag == "example-sentences":
                self.example_sentences = element

    def unpack_cn_custom_translation(self):
        if len(self.custom_translation) >= 1:
            for child in self.custom_translation[0]:
                if child.tag == "translation":
                    self.cn_translation.append(child[0].text)
                elif child.tag == "word-forms":
                    for element in child:
                        self.all_word_forms.append(element)

    def word_forms(self):        
        elements_wordforms = {}
        for x in self.all_word_forms:
            i = 0
            while i < len(x):
                if x[i].tag == "value":
                    elements_wordforms[x[i-1].text] = x[i].text
                i = i + 1
        return elements_wordforms

    def speak(self):
        audiofile = os.getenv("HOME") + "/.ldict/audio/" + self.word_quote + ".mp3"
        if os.path.exists(audiofile) != True:
            mp3 = urllib2.urlopen(self.speak_link, None, 0.5).read()
            f = open(audiofile, 'w')
            f.write(mp3)
            f.close()
            
        import gst
        import gobject

        def on_eos(bus, msg):
            bin.set_state(gst.STATE_NULL)
            mainloop.quit()

        audiofile = "file://"+ audiofile
        bin = gst.element_factory_make("playbin")
        bin.set_property("uri", audiofile)
        bin.set_state(gst.STATE_PLAYING)
        bus = bin.get_bus()
        bus.add_signal_watch()
        bus.connect('message::eos', on_eos)
        mainloop = gobject.MainLoop()
        mainloop.run()
        
    def example_sentence(self):
        sentences = {}
        i = 0
        for x in self.example_sentences:
            if i < 3:
                sentences[x[0].text] = x[2].text
                i = i + 1
        return sentences
