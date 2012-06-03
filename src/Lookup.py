#! /usr/bin/python
# -*- coding: utf-8 -*-
import re
import urllib
import urllib2
import sys
import os

def look_up(word):    
    res = translate(word)
    return res

def get_elements_by_path(xml, elem):
    if type(xml) == type(''):
        xml = [xml]
    if type(elem) == type(''):
        elem = elem.split('/')
    if (len(xml) == 0):
        return []
    elif (len(elem) == 0):
        return xml
    elif (len(elem) == 1):
        result = []
        for item in xml:
            result += get_elements(item, elem[0])
        return result
    else:
        subitems = []
        for item in xml:
            subitems += get_elements(item, elem[0])
        return get_elements_by_path(subitems, elem[1:])
    
textre = re.compile("\!\[CDATA\[(.*?)\]\]", re.DOTALL)

def get_text(xml):
    match = re.search(textre, xml)
    if not match:
        return xml
    return match.group(1)

def get_elements(xml, elem):
    p = re.compile("<" + elem + ">" + "(.*?)</" + elem + ">", re.DOTALL)
    it = p.finditer(xml)
    result = []
    for m in it:
        result.append(m.group(1))
    return result

def translate(word):
    sword = str(word)
    word = word.toLower()
    word = str(word)
    word = word.strip()
    
   # print word
    res = u"<div style=\"font-family:Ubuntu\"><center><p><span style=\"font-size:25px; font-weight:bold; color:#000;\">" + sword + "</span>"
    if os.path.exists("./dictxml/"+word+".xml"):
        file_path = "./dictxml/"+word+".xml"
        #xml = urllib.urlopen(file_path, None, 0.5).read()
        xml = open(file_path).read()
    else:
        try:
            xml = urllib2.urlopen("http://dict.yodao.com/search?keyfrom=lindict&q="
                                  + urllib.quote_plus(str(word)) + "&xmlDetail=true&doctype=xml",None,0.5).read();
        except:
            xml=None
    if xml!=None:
        #prounounce
        prou=get_elements(xml, "phonetic-symbol")
        if len(prou)>0:
            prou=get_text(prou[0])
            if len(prou)>0:
                res+="<span style=\"font-size:15px; color:#0000b1;\">   ["+prou+"]</span>"
        res += "</p></center>"    
        
        #word form
        wordforms=get_elements(xml, "word-form")
        if len(wordforms)>0:
            res+="<p>"
            for wordform in wordforms:
                formname=get_elements(wordform, "name")
                res+=get_text(formname[0])+": "
                formname=get_elements(wordform, "value")
                res+=get_text(formname[0])+"&nbsp;&nbsp;&nbsp;&nbsp;"
            res+="</p>"    
            
        #ec trans  
        custom_translations = get_elements(xml, "custom-translation")
        if len(custom_translations)>0:
            ectrans=custom_translations[0]
            src=get_elements_by_path(ectrans, "source/name")
            if len(src)>0:
                res+="<p style=\"color:#2555B4\">"+get_text(src[0])+"</p>"        
            trans=get_elements_by_path(ectrans, "translation/content")
            res+="<ul>"
            for tran in trans:
                res+="<li>"+get_text(tran)+"</li>"
            res+="</ul>"
        
    #Jinshan
    try:
        jinshan = urllib2.urlopen("http://dict-co.iciba.com/api/dictionary.php?w="+urllib.quote_plus(str(word)),None,0.5).read()
    except:
        jinshan=None
    if jinshan!=None:
        jin_word= get_elements(jinshan, "pos")
        jin_word_b=get_elements(jinshan, "acceptation")
        if len(jin_word)>0:
            res+=u"<p style=\"color:#2555B4\">œðÉœŽÊ°Ô</p><ul>"
            for i in range(0,len(jin_word)):
                res+="<li>"+get_text(jin_word[i])+" "
                res+=get_text(jin_word_b[i])+"</li>"
            res+="</ul>"
        
    # phrase
    if xml!=None:
        yodao_translations = get_elements(xml, "yodao-web-dict")
        if len(yodao_translations)>0:
            res+=u"<p style=\"color:#2555B4\">词组</p><ul>"        
            for trans in yodao_translations:
                webtrans = get_elements(trans, "web-translation")
                for web in webtrans[0:50]:
                    keys = get_elements(web, "key")
                    values = get_elements_by_path(web, "trans/value")
                    summaries = get_elements_by_path(web, "trans/summary")
                    key = keys[0].strip()
                    value = values[0].strip()
                    res+= "<li>"+get_text(key) + ":\t" + get_text(value)+"</li>";
            res+="</ul>"
    
    #jinshan sents
    if jinshan!=None:
        sents=get_elements(jinshan, "sent") 
        if len(sents)>0: 
            res+=u"<p style=\"color:#2555B4\">Ï°Óï</p><ul>"
            for sent in sents:
                res+="<li>"+get_text(get_elements(sent, "orig")[0])
                res+="<br/>"+get_text(get_elements(sent, "trans")[0])+"</li>"
            res+="</ul>"
        
    #sentence
    if xml!=None:
        sents=get_elements(xml, "sentence-pair")
        if len(sents)>0:
            res+=u"<p style=\"color:#2555B4\">句子</p><ul>" 
            for sent in sents:
                res+="<li>"+get_text(get_elements(sent, "sentence")[0])
                res+="<br/>"+get_text(get_elements(sent, "sentence-translation")[0])+"</li>"
            res+="</ul>"
        
        #cc trans
        custom_translations = get_elements(xml, "custom-translation")
        if len(custom_translations)>1:
            ectrans=custom_translations[1]
            src=get_elements_by_path(ectrans, "source/name")
            if len(src)>0:
                res+="<p style=\"color:#2555B4\">"+get_text(src[0])+"</p>"        
            trans=get_elements_by_path(ectrans, "translation/content")
            res+="<ul>"
            for tran in trans:
                res+="<li>"+get_text(tran)+"</li>"
            res+="</ul>"
                 
    res+="</div>"
    return res
