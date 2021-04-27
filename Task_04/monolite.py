# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:04:14 2021
@author: User
"""
from datetime import datetime as dt
from datetime import timedelta as td
import abc
from pathlib import Path
import sys
import tkinter as tk
from tkinter import filedialog
import os
from os import path

#Use strategy pattern here:
class PublisherManager:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self, publication):
        self.object = publication
        self._strategy.publication_interface(self.object)

class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def publication_interface(self, publication):
        pass

class NotePublisher:
    def publication_interface(self, publication):
        city_name = publication.city
        text_tweet = publication.text
        publication_date = publication.date
        publication_header = publication.header
        
        with open("D:\\proc\\notes.txt", "a") as a_file:
            a_file.write(f'{publication_header}')
            a_file.write(f'{text_tweet}\n{city_name}, {publication_date}\n' )
            a_file.write("\n")
    
class ConfidentialPublisher:
    def publication_interface(self, publication):
        text_tweet = publication.text
        days_left = publication.daysleft
        publication_header = publication.header
        date_1 = dt.strptime(publication.date, "%d/%m/%Y %H.%M")                        
        end_date = f'{(date_1 + td(days=days_left)).strftime("%d/%m/%Y")}'
        day_ending = "day" if days_left == 1 else "days"        
        with open("D:\\proc\\notes.txt", "a") as a_file:
            a_file.write(f'{publication_header}')
            a_file.write(f'{text_tweet}\nActual until: {end_date}, {publication.daysleft} {day_ending} left\n' )
            a_file.write("\n")

class JokePublisher:
    def publication_interface(self, publication):
        city_name = publication.city
        text_tweet = publication.text
        publication_date = publication.date
        publication_header = publication.header
        with open("D:\\proc\\notes.txt", "a") as a_file:
            a_file.write(f'{publication_header}')
            a_file.write(f'{city_name}\n{text_tweet}\n{publication_date}\n' )
            a_file.write("\n")

class DumpPublisher:
    def publication_interface(self, publications:list):
        for item in publications:
            city_name = item.city
            text_tweet = item.text
            publication_date = item.date
            publication_header = item.header
            with open("D:\\proc\\notes.txt", "a") as a_file:
                a_file.write(f'{publication_header}')
                a_file.write(f'{city_name}\n{text_tweet}\n{publication_date}\n' )
                a_file.write("\n")                    
                
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
        self.__daysleft += Publication.__typeTestInt(daysleft)
        
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
    
# class Human:
class Human:
    def __init__(self, age):
        self.age = age
        
# class Author:
class Author(Human):
    def __init__(self, name, **mydict):
        super().__init__(**mydict)
        self.name = name
        
# class User:      
class User(Author):    
    def __init__(self, name, age, max_number):
        self.name = name
        self.age = age
        self.max_number_of_publications = max_number
        self.counter = 0
        self.publications = []
        super().__init__(age=age, name=name)
    def __repr__(self):
        return "name: {}, age: {}, max_number_of_publications: {}".format(
                self.age, 
                self.name, 
                self.max_number_of_publications)    
    def add_publication(self, publication):
        self.counter = self.counter + 1
        if len(self.publications) < self.max_number_of_publications:
            self.publications.append(publication)
            ptype = publication.publicationtype
            if ptype == "note":
                publication.header = "Note-------------------------\n"
                note_publisher = NotePublisher()
                context = PublisherManager(note_publisher)
                context.context_interface(publication)
            if ptype == "joke":
                publication.header = "Joke of the day--------------\n"
                joke_publisher = JokePublisher()
                context = PublisherManager(joke_publisher)
                context.context_interface(publication)
            if ptype == "confidential":
                publication.header = "Confidential tweet-----------\n"
                confidential_publisher = ConfidentialPublisher()
                context = PublisherManager(confidential_publisher)
                context.context_interface(publication)
            return True
        else:
            print(f"You publication {self.counter} in aborted!")
            return False

class PipelineDataManager:
    
    def define_number_of_publications(number):
        return number
    
    def generate_initial_data():
        list_of_publications = []
        #1.User select what data type he wants to add(note, joke or personal tweet)
        n1 = Publication("note", "London", "Hello, world" )
        n2 = Publication("joke", "Moscow", "Hello, world")
        n3 = Publication("confidential", "Minsk", "Hello, world", 21)
        n4 = Publication("note", "New_York", "Hello, world")
        
        list_of_publications.append(n1)
        list_of_publications.append(n2)
        list_of_publications.append(n3)
        list_of_publications.append(n4)
        
        return list_of_publications
    
    def add_generated_data_to_list(list_of_publications:list):
        for i in list_of_publications:
            user.add_publication(i)


class FileManager:
    
    def __init__(self):
        self.__file_path = FileManager.create_file_path()
        
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
    
    def create_file_path():
        repository = RepositoryManager()
        directory = repository.define_directory()
        my_file_path = os.path.join(directory,"notes.txt")
        return my_file_path
    
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
        super().__init__() #give path to base class reader
        self.header = header
        self.text_second_row = text_second_row
        self.text_third_row = text_third_row
        self.text_fourth_row = text_fourth_row    
        
    def read_file(self):
        my_file = Path(self.file_path)
        if my_file.exists():
            try:
                f = open(my_file, "r")
                text = f.read()
                f.close()
                result_text_list = TextFileManager.readme(text)
                print("Reading from files results:\n\n****************************\n")
                try:
                    for i in result_text_list:
                        print(f'{i.header}\n{i.text_second_row}\n{i.text_third_row}\n{i.text_fourth_row}\n')
                except TypeError:
                    print("Object is not iterable")
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                TextFileManager.delete_file(my_file)
            except FileNotFoundError as error:
                print(error)        
        
    def readme(text):
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
                    out.append(TextFileManager(header, text_second_row, text_third_row, text_fourth_row))
                    n = 0
                else:
                    out.append(TextFileManager(header, text_second_row, text_third_row, text_fourth_row=None))
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
    
    def dump_data_from_memory_to_file(self, publication_collection):
        dump_publisher = DumpPublisher()
        context = PublisherManager(dump_publisher)
        context.context_interface(publication_collection)

    def delete_file(my_file):
        os.remove(my_file)


class RepositoryManager:
    
    def __init__(self):
        self.__default_directory_path = RepositoryManager.create_path()
    
    def create_path():
        directory_path = "D:\\proc"
        return directory_path
    
    def create_directory():
        os.makedirs(self.__default_directory_path)
        
    def rename_directory(newname):
        os.rename(self.__default_directory_path, newname)
    
    def delete_directory():
        os.remove(self.__default_directory_path)
    
    @property
    def default_directory_path(self):
        return self.__default_directory_path
    
    @default_directory_path.setter
    def default_directory_path(self, str):
        self.__default_directory_path += PathWorker.__typeTest(str)
    
    @staticmethod
    def __typeTest(value):
        if isinstance(value, str):
            return value
        else:
            raise TypeError('Must be string type')
        
    def define_directory(self):
        counter = 0
        result = path.exists(self.default_directory_path)
        print(f'result {counter}')
        if result:
            return self.__default_directory_path
        else:
            root = tk.Tk()
            root.withdraw()
            user_choosed_directory = filedialog.askdirectory()
            self.__default_directory_path = user_choosed_directory
            return self.__default_directory_path

#Test area:
def main():
    pass
    
if __name__ == "__main__":
    
    user = User("Anton", 34, PipelineDataManager.define_number_of_publications(3))
    list_of_publications = PipelineDataManager.generate_initial_data()
    PipelineDataManager.add_generated_data_to_list(list_of_publications)
    textFileManager = TextFileManager()
    textFileManager.dump_data_from_memory_to_file(user.publications)
    #textFileManager.read_file()
    main()