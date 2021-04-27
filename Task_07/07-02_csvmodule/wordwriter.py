# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:33:59 2021

@author: User
"""
from filewriter import*
import csv

class WordWriter(FileWriter):
    def write_me_words(sorted_list:list):
        myFile = open('D:\\proc\\testdir\\test2.csv', 'w', newline='')
        with myFile:
            myFields = ['word', 'count']
            writer = csv.DictWriter(myFile, delimiter=',', fieldnames=myFields)    
            writer.writeheader()
            for k, v in sorted_list.items():
                writer.writerow({'word': k, 'count': v})


