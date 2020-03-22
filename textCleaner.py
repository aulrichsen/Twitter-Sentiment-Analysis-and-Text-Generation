# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 09:54:19 2020

@author: qwb15130
"""

import re

def textCleaner(text):
    username_re = re.compile(r'[@]\S*')
    url_re = re.compile(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\(['
                    r'^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,'
                    r'<>?\xab\xbb\u201c\u201d\u2018\u2019]))')

    #text = open(file,encoding='latin-1').read()

    text = re.sub(username_re, '@username', text)
    text = re.sub(url_re, '@url', text)
    text = re.sub("&amp", '&', text)
    text = re.sub('"', '', text)
    
    return text