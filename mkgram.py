#!/usr/bin/env python
# encoding: utf-8
"""
mkgram.py

Created by Stephen Holiday on 2011-04-21.
Copyright (c) 2011.
Apache License Version 2.0
"""

import sys
import os
import nltk
import stringCleaner
import re

def string_to_token_list(string,stopwords=False):
    string=string.lower()

    tokens_raw = re.findall('[a-zA-Z0-9\-\'\`\+]+',string)

    #lowercase them
    words=map(lambda x: stringCleaner.safe_unicode(x.lower()),tokens_raw)

    #if we want to remove the stop words...
    tokens=list()
    if stopwords:
        stop_words = nltk.corpus.stopwords.words('english')
        for word in words:
            if not word in stop_words:
                tokens.append(word)
    else:
        tokens=words
    return tokens


def token_list_to_dict(token_list):
    tokens=dict()
    for token in token_list:
        if not tokens.has_key(token):
            tokens[token]=1
        else:
            tokens[token]+=1
    return tokens

def token_list_to_bigrams(token_list):
    tokens=dict()
    for i in xrange(0,len(token_list)-2):
        token=token_list[i]+' '+token_list[i+1]
        if not tokens.has_key(token):
            tokens[token]=1
        else:
            tokens[token]+=1
    return tokens
    
def token_list_to_trigrams(token_list):
    tokens=dict()
    for i in xrange(0,len(token_list)-3):
        token=token_list[i]+' '+token_list[i+1]+' '+token_list[i+2]
        if not tokens.has_key(token):
            tokens[token]=1
        else:
            tokens[token]+=1
    return tokens
def token_list_to_quadgrams(token_list):
    tokens=dict()
    for i in xrange(0,len(token_list)-4):
        token=token_list[i]+' '+token_list[i+1]+' '+token_list[i+2]+' '+token_list[i+3]
        if not tokens.has_key(token):
            tokens[token]=1
        else:
            tokens[token]+=1
    return tokens
    
def sort_tokens(tokens):
    return sorted(tokens,key=lambda x : tokens[x],reverse=False)