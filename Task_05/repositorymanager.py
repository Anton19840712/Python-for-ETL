# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:38:02 2021

@author: User
"""
from os import path 
import tkinter as tk
from tkinter import filedialog

class RepositoryManager:
    
    def __init__(self):
        self.__default_directory_path = RepositoryManager.create_path()
    
    def create_path():
        directory_path = "D:\\prroc"
        return directory_path
    
    def create_directory():
        os.makedirs(RepositoryManager.create_path())
        
    def rename_directory(newname):
        os.rename(RepositoryManager.create_path(), newname)
    
    def delete_directory():
        os.remove(RepositoryManager.create_path())
    
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