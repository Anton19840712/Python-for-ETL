# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:33:58 2021

@author: User
"""
import csv
from filewriter import*
class CharsWriter(FileWriter):
    def write_me_chars(data_scope_from_cooker:list, sum_of_values:int, upper_results:int):
        myFile = open('D:\\proc\\testdir\\test.csv', 'w', newline='')
        with myFile:
            myFields = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(myFile, delimiter=',', fieldnames=myFields)    
            writer.writeheader()
            for k, v in data_scope_from_cooker.items():
                writer.writerow({'letter': k, 'count_all': len(data_scope_from_cooker.items()), 'count_uppercase': upper_results, 'percentage' : str(round(v/sum_of_values*100,3))+" %"})