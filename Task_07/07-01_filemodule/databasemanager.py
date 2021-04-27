# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 04:12:35 2021

@author: User
"""
from tablewriter import*
class DataBaseManager:
        
    def edit_table(list_of_publications:list):
        for element in list_of_publications:
            in_label = str(element).split(",")[0].split(': ')[1] #getting note_label  from list_of_publications
            if in_label == "note":
                note_table_writer = NoteTableWriter()
                context = TableWriter(note_table_writer)
                context.context_interface(element, in_label)                
            if in_label == "joke":
                joke_table_writer = JokeTableWriter()
                context = TableWriter(joke_table_writer)
                context.context_interface(element, in_label)
            if in_label == "confidential":
                confidential_table_writer = ConfidentialTableWriter()
                context = TableWriter(confidential_table_writer)
                context.context_interface(element, in_label)