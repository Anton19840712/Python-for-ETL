# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:34:00 2021

@author: User
"""
class WordsReader():
    def word_count(str):
        counts = dict()
        words = str.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts