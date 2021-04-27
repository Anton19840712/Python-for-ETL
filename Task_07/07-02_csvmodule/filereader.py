# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:34:00 2021

@author: User
"""
class FileReader():
    def read_files_data(path_names:list):
        common_string = ""
        for file in path_names:
            string = open(file).read()
            common_string = common_string + string
        return common_string
    