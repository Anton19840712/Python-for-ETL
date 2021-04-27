# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:35:45 2021

@author: User
"""
from datetime import datetime as dt

class Publication:
    def __init__(self, publicationtype, city=None, text=None, daysleft=None, header = None):
        self.__header = header  
        self.__publicationtype = publicationtype    
        self.__city = city
        self.__text = text
        self.__daysleft = daysleft
        self.__date = f'{dt.now().strftime("%d/%m/%Y %H.%M")}'
        
    @property
    def header(self):
        return self.__header
    
    @header.setter
    def header(self, value):
        self.__header = value
        
    @property
    def publicationtype(self):
        return self.__publicationtype
    
    @publicationtype.setter
    def publicationtype(self, str):
        self.__publicationtype += Publication.__typeTest(str)
       
    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, str):
        self.__city += Publication.__typeTest(str)
        
    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, str):
        self.__text += Publication.__typeTest(str)  
        
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, datetime):
        self.__date += Publication.__typeTestDate(datetime)
    
    @property
    def daysleft(self):
        return self.__daysleft
    
    @daysleft.setter
    def daysleft(self, int):
        self.__daysleft += Publication.__typeTestInt(int)
        
    @staticmethod
    def __typeTest(value):
        if isinstance(value, str):
            return value
        else:
            raise TypeError('Must be a string type')
            
    @staticmethod
    def __typeTestDate(value):
        if isinstance(value, datetime):
            return value
        else:
            raise TypeError('Must be a datetime type')
            
    @staticmethod
    def __typeTestInt(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Must be an int type')  
            
    def __repr__(self):
        return "city: {}, text: {}, date: {}".format(
                self.city, 
                self.text, 
                self.date) 
