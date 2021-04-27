# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:34:01 2021

@author: User
"""
class CharsReader():
    def count_chars_pool(newnewstring:str):
        all_freq = {}
  
        for i in newnewstring:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
        return all_freq