# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:37:43 2021

@author: User
"""
from pathlib import Path
import os
from publisher import*
class FileManager:     
    def __init__(self, mypath):
        self.__file_path = mypath
        
    @property
    def file_path(self):
        return self.__file_path
    
    @file_path.setter
    def file_path(self, str):
        self.__file_path += FileManager.__typeTest(str)
        
    @staticmethod
    def __typeTest(value):
        if isinstance(value, str):
            return value
        else:
            raise TypeError('Must be string type')
    
    def read_file(self):
        pass
    
    def write_file(self):
        pass
    
    def dump_data_from_memory_to_file(self):
        pass
    
    def create_file(self):
        pass
    
    def rename_file(self):
        pass
    
    def delete_file(self):
        pass


class TextFileManager(FileManager):
    def __init__(self, header=None, text_second_row=None, text_third_row=None, text_fourth_row=None): 
        super().__init__(self)
        self.header = header
        self.text_second_row = text_second_row
        self.text_third_row = text_third_row
        self.text_fourth_row = text_fourth_row    
        
    def read_file(self, mypath):
        my_file = Path(mypath)
        if my_file.exists():
            try:
                f = open(my_file, "r")
                text = f.read()
                f.close()
                result_text_list = self.readme(text)
                print("Reading from files results:\n\n****************************\n")
                try:
                    for i in result_text_list:
                        print(f'{i.header}\n{i.text_second_row}\n{i.text_third_row}\n{i.text_fourth_row}\n')
                except TypeError:
                    print("Object is not iterable")
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                self.delete_file(my_file)
            except FileNotFoundError as error:
                print(error)        
        
    def readme(self, text):
        try: 
            clean_data = map(str.strip, text.splitlines())
            out = []
            n = 1
            for i in clean_data:
                if n == 1:
                    header = i
                elif n == 2:
                    text_second_row = i
                elif n == 3:
                    text_third_row = i
                elif n == 4 and i != "\n":
                    text_fourth_row = i
                    out.append(TextFileManager(header, text_second_row, text_third_row, text_fourth_row))
                    n = 0
                else:
                    out.append(TextFileManager(header, text_second_row, text_third_row))
                    n = 0
                n += 1
            return out
        except ValueError as error:
            print(error)
        except AttributeError as error:
            print(error)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise        
    
    def dump_data_from_memory_to_file(self, publication_collection, mypath):
        dump_publisher = DumpPublisher()
        context = Publisher(dump_publisher)
        context.context_interface(publication_collection, mypath)

    def delete_file(self, my_file):
        os.remove(my_file)