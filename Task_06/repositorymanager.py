# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:34:01 2021

@author: User
"""
from os import walk
from os import path
import tkinter as tk
from tkinter import filedialog

class RepositoryManager():
    def __init__(self):
        self.__default_directory_path = RepositoryManager.create_path()
    def gain_me_file_names():
        file_list = []
        # this is derictory, where your files should be by default to take smoke test of my application. 
        # Or you can change it manually here to test my code. This is my copy from the previos Task 05. There it works fine, but I need to learn myself now) Tnank u))
        for (dirpath, dirnames, filenames) in walk('D:\\proc\\testdir'):
            file_list.extend(filenames)
        return file_list
    def gain_me_path_list(file_list:list):
        path_list =[]
        for filename in file_list:
            full_pathes = path.join('D:\\proc\\testdir', filename)
            path_list.append(full_pathes)
        return path_list
    def create_path():
        directory_path = "D:\\prroc"
        return directory_path    
    @property
    def default_directory_path(self):
        return self.__default_directory_path
    
    @default_directory_path.setter
    def default_directory_path(self, str):
        self.__default_directory_path += RepositoryManager.__typeTest(str)
    
    @staticmethod
    def __typeTest(value):
        if isinstance(value, str):
            return value
        else:
            raise TypeError('Must be string type')
        
    def define_directory(self):
        result = path.exists(self.default_directory_path)
        print(result)
        if result:
            return self.__default_directory_path
        else:
            root = tk.Tk()
            root.withdraw()
            user_choosed_directory = filedialog.askdirectory()
            self.__default_directory_path = user_choosed_directory
            return self.__default_directory_path