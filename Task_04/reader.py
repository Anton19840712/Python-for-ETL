# -*- coding: utf-8 -*-
"""  
Created on Sat Mar 27 22:55:01 2021

@author: User
"""
#use strategy pattern here
from pathlib import Path
class ContentReader:
    def __init__(self, header, text_second_row, text_third_row, text_fourth_row=None):
        self.header = header
        self.text_second_row = text_second_row
        self.text_third_row = text_third_row
        self.text_fourth_row = text_fourth_row
 
    def read(text):
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
                elif n == 4 and i!="":
                    text_fourth_row = i
                    out.append(ContentReader(header, text_second_row, text_third_row, text_fourth_row))
                    n = 0
                else:
                    out.append(ContentReader(header, text_second_row, text_third_row, text_fourth_row=None))
                    n = 0
                n += 1
            # here we have parsed to list our data file
            return out
        except ValueError as error:
            print(error)
        except AttributeError as error:
            print(error)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def read_from_file():
        #hardcode with path
        my_file = Path("D:\\proc\\notes.txt")
        if my_file.exists():
            try:
                f = open("D:\\proc\\notes.txt", "r")
                text = f.read()
                f.close()
                return text
            except FileNotFoundError as error:
                print(error)