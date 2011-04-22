#!/usr/bin/env python
# encoding: utf-8
"""
stringCleaner.py

Created by Stephen Holiday on 2011-04-21.
Copyright (c) 2011. All rights reserved.
"""

class stringCleaner():
    def safe_unicode(obj): # Converts a string easily
        try:
            return str(obj)
        except UnicodeEncodeError:
            # obj is unicode
            return unicode(obj).encode('utf-8')
    def remove_tags(data):
        p = re.compile(r'<.*?>')
        return p.sub('', data)