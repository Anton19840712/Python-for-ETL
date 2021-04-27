# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 04:10:24 2021

@author: User
"""
import abc
import pyodbc

class TableWriter:
    def __init__(self, strategy):
        self._strategy = strategy
    def context_interface(self, element, in_label):
        self.element = element
        self.label = in_label
        self._strategy.publication_interface(element, in_label)

class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def publication_interface(element, in_label):
        pass

class NoteTableWriter:
    def publication_interface(self, element, in_label):
        note_city = str(element).split(",")[1].split(': ')[1]      
        note_tweet = str(element).split(": ")[3].rsplit(' ', 1)[0][:-1]
        # glue them, getting composite key
        string_from_list_of_publications = in_label + note_city + note_tweet
        fileSpec = r"D:\test\test.db"
        connection = pyodbc.connect("DRIVER={SQLite3 ODBC Driver};Direct=True; String Types = Unicode; DATABASE="+fileSpec)
        cursor = connection.cursor()
        creation_parameters = ("note", "label", "city", "tweet")
        cursor.execute("""CREATE TABLE IF NOT EXISTS %s (%s text, %s text, %s text)"""% creation_parameters)
        cursor.execute("""SELECT * FROM %s""" %in_label)
        result = cursor.fetchall() 
        if len(result) == 0:
            var1 = str(in_label)
            var2 = str(note_city)
            var3 = str(note_tweet)                        
            cursor.execute("INSERT INTO note VALUES (?, ?, ?)", (var1, var2, var3))
            connection.commit()
        else:
            database_glued_elements_list = []
            for element_database in result:
                item = ''
                for i in element_database:
                    item = item + str(i) #glue this row in database composite key
                database_glued_elements_list.append(item)
            if not (string_from_list_of_publications in database_glued_elements_list):#check if current element from list_of_publications exists in database_glued_elements_list
                var1 = str(in_label)
                var2 = str(note_city)
                var3 = str(note_tweet)
                cursor.execute("INSERT INTO note VALUES (?, ?, ?)", (var1, var2, var3))
                connection.commit()

class JokeTableWriter():
    def publication_interface(self, element, in_label):
        joke_city = str(element).split(",")[1].split(': ')[1]      
        joke_tweet = str(element).split(": ")[3].rsplit(' ', 1)[0][:-1]
        # glue them, getting composite key
        string_from_list_of_publications = in_label + joke_city + joke_tweet
        fileSpec = r"D:\test\test.db"
        connection = pyodbc.connect("DRIVER={SQLite3 ODBC Driver};Direct=True; String Types = Unicode; DATABASE="+fileSpec)
        cursor = connection.cursor()
        creation_parameters = ("joke", "label", "city", "tweet")
        cursor.execute("""CREATE TABLE IF NOT EXISTS %s (%s text, %s text, %s text)"""% creation_parameters)
        cursor.execute("""SELECT * FROM %s""" %in_label)
        result = cursor.fetchall() 
        if len(result) == 0:
            var1 = str(in_label)
            var2 = str(joke_city)
            var3 = str(joke_tweet)                        
            cursor.execute("INSERT INTO joke VALUES (?, ?, ?)", (var1, var2, var3))
            connection.commit()
        else:
            database_glued_elements_list = []
            for element_database in result:
                item = ''
                for i in element_database:
                    item = item + str(i) #glue this row in database composite key
                database_glued_elements_list.append(item)
            if not (string_from_list_of_publications in database_glued_elements_list):#check if current element from list_of_publications exists in database_glued_elements_list
                var1 = str(in_label)
                var2 = str(joke_city)
                var3 = str(joke_tweet)
                cursor.execute("INSERT INTO joke VALUES (?, ?, ?)", (var1, var2, var3))
                connection.commit()

class ConfidentialTableWriter():
    def publication_interface(self, element, in_label):
        confidential_tweet = str(element).split(": ")[3].rsplit(' ', 1)[0][:-1]
        confidential_date = str(element).split(": ")[4]
        # glue them, getting composite key
        string_from_list_of_publications = in_label + confidential_tweet + confidential_date
        fileSpec = r"D:\test\test.db"
        connection = pyodbc.connect("DRIVER={SQLite3 ODBC Driver};Direct=True; String Types = Unicode; DATABASE="+fileSpec)
        cursor = connection.cursor()
        creation_parameters = ("confidential", "label", "tweet", "date")
        cursor.execute("""CREATE TABLE IF NOT EXISTS %s (%s text, %s text, %s text)"""% creation_parameters)
        cursor.execute("""SELECT * FROM %s""" %in_label)
        result = cursor.fetchall() 
        if len(result) == 0:
            var1 = str(in_label)
            var2 = str(confidential_tweet)
            var3 = str(confidential_date)                        
            cursor.execute("INSERT INTO confidential VALUES (?, ?, ?)", (var1, var2, var3))
            connection.commit()
        else:
            database_glued_elements_list = []
            for element_database in result:
                item = ''
                for i in element_database:
                    item = item + str(i) #glue this row in database composite key
                database_glued_elements_list.append(item)
            if not (string_from_list_of_publications in database_glued_elements_list):#check if current element from list_of_publications exists in database_glued_elements_list
                var1 = str(in_label)
                var2 = str(confidential_tweet)
                var3 = str(confidential_date)
                cursor.execute("INSERT INTO note VALUES (?, ?, ?)", (var1, var2, var3))
                connection.commit()