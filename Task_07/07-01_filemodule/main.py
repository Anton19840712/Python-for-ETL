# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:04:14 2021
@author: User
"""
import datetime
import sys
import sqlite3
from human import*
from repositorymanager import*
from publisher import*
from human import*
from filemanager import*
from publication import*
from datetime import datetime as dt
from databasemanager import*

class PipelineDataManager: 
    def generate_initial_data():
        list_of_publications = []
        n1 = Publication("note", "London", "Hello, world" )
        n2 = Publication("joke", "Moscow", "Hello, world")
        n3 = Publication("confidential", "Minsk", "Hello, world", 21)
        n4 = Publication("note", "New_York", "Hello, world")        
        list_of_publications.append(n1)
        list_of_publications.append(n2)
        list_of_publications.append(n3)
        list_of_publications.append(n4) 
        return list_of_publications
    def add_generated_data_to_publications_list(list_of_publications:list, mypath):
        for i in list_of_publications:
            user.add_publication(i, mypath)
#Test area:
def main():
    pass
    
if __name__ == "__main__":    
    user = User("Anton", 34, 3)    
    list_of_publications = PipelineDataManager.generate_initial_data()    
    DataBaseManager.edit_table(list_of_publications)        
    directory = RepositoryManager().define_directory()       
    my_file_path = os.path.join(directory + "/", "notes.txt")
    PipelineDataManager.add_generated_data_to_publications_list(list_of_publications, my_file_path)
    fileManager = FileManager(my_file_path)
    textFileManager = TextFileManager()
    textFileManager.dump_data_from_memory_to_file(user.publications, my_file_path)
    # textFileManager.read_file(my_file_path)
    main()