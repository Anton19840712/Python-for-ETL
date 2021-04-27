# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 04:22:32 2021

@author: User
"""
            
import pyodbc
from operator import itemgetter

class DataBaseManager:    
    def write_words_to_database(sorted_list:list):
        in_label = "word"
        fileSpec = r"D:\test\test.db"
        connection = pyodbc.connect("DRIVER={SQLite3 ODBC Driver};Direct=True; String Types = Unicode; DATABASE="+fileSpec)
        cursor = connection.cursor()
        creation_parameters = ("word", "word", "count")
        cursor.execute("""CREATE TABLE IF NOT EXISTS %s (%s text, %s int)"""% creation_parameters)
        cursor.execute("""SELECT * FROM %s""" %in_label)
        result = cursor.fetchall()
        if len(result) == 0:
            for k, v in sorted_list.items():
                var1 = str(k)
                var2 = str(v)                      
                cursor.execute("INSERT INTO word VALUES (?, ?)", (var1, var2))
                connection.commit()
        else:
            database_glued_elements_list = []
            for element_database in result:
                item = ''
                for i in element_database:
                    item = item + str(i) #glue this row in database as composite key
                database_glued_elements_list.append(item)
            for state, capital in sorted_list.items():
                string_from_analyzed_files = state+str(capital)
                if not (string_from_analyzed_files in database_glued_elements_list):#check if current element from list_of_publications exists in database_glued_elements_list
                    var1 = str(k)
                    var2 = str(v)
                    cursor.execute("INSERT INTO note VALUES (?, ?)", (var1, var2))
                    connection.commit()

    def write_chars_to_database(data_scope_from_cooker:list, sum_of_values:int, upper_results:int):
        print(data_scope_from_cooker)
        in_label = "char"
        fileSpec = r"D:\test\test.db"
        connection = pyodbc.connect("DRIVER={SQLite3 ODBC Driver};Direct=True; String Types = Unicode; DATABASE="+fileSpec)
        cursor = connection.cursor()
        creation_parameters = ("char", "letter", "count_all", "count_uppercase", "percentage")
        cursor.execute("""CREATE TABLE IF NOT EXISTS %s (%s text, %s int, %s int, %s float)"""% creation_parameters)
        cursor.execute("""SELECT * FROM %s""" %in_label)
        result = cursor.fetchall()
        if len(result) == 0:
            count_all = len(data_scope_from_cooker.items())
            for k, v in data_scope_from_cooker.items():
                var1 = str(k)
                var2 = count_all
                var3 = upper_results
                var4 = (round(v/sum_of_values*100,3))                
                cursor.execute("INSERT INTO char VALUES (?, ?, ?, ?)", (var1, var2, var3, var4))
                connection.commit()
        else:
            database_glued_elements_list = []
            for element_database in result:
                item = itemgetter(0, -1)(element_database)                
                item1 = int(round(item[-1]*sum_of_values/100, 0))
                item2 = item[0]
                item = str(item2) + str(item1)
                database_glued_elements_list.append(item)
            for state, capital in data_scope_from_cooker.items():
                string_from_analyzed_files = state+str(capital)
                if not (string_from_analyzed_files in database_glued_elements_list):#check if current element from list_of_publications exists in database_glued_elements_list
                    var1 = str(k)
                    var2 = str(v)
                    cursor.execute("INSERT INTO note VALUES (?, ?)", (var1, var2))
                    connection.commit()          
                
