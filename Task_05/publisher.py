# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:35:11 2021

@author: User
"""
import abc
from datetime import datetime as dt
from datetime import timedelta as td
#Use strategy pattern here:
class Publisher:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self, publication, mypath):
        self.object = mypath
        self.object = publication
        self._strategy.publication_interface(self.object, mypath)

class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def publication_interface(self, publication, mypath):
        pass

class NotePublisher:
    def publication_interface(self, publication, mypath):
        city_name = publication.city
        text_tweet = publication.text
        publication_date = publication.date
        publication_header = publication.header
        with open(mypath, "a") as a_file:
            a_file.write(f'{publication_header}')
            a_file.write(f'{text_tweet}\n{city_name}, {publication_date}\n' )
            a_file.write("\n")
    
class ConfidentialPublisher:
    def publication_interface(self, publication, mypath):
        text_tweet = publication.text
        days_left = publication.daysleft
        publication_header = publication.header
        date_1 = dt.strptime(publication.date, "%d/%m/%Y %H.%M")                        
        end_date = f'{(date_1 + td(days=days_left)).strftime("%d/%m/%Y")}'
        day_ending = "day" if days_left == 1 else "days"        
        with open(mypath, "a") as a_file:
            a_file.write(f'{publication_header}')
            a_file.write(f'{text_tweet}\nActual until: {end_date}, {publication.daysleft} {day_ending} left\n' )
            a_file.write("\n")

class JokePublisher:
    def publication_interface(self, publication, mypath):
        city_name = publication.city
        text_tweet = publication.text
        publication_date = publication.date
        publication_header = publication.header
        with open(mypath, "a") as a_file:
            a_file.write(f'{publication_header}')
            a_file.write(f'{city_name}\n{text_tweet}\n{publication_date}\n' )
            a_file.write("\n")

class DumpPublisher:
    def publication_interface(self, publications:list, mypath):
        for item in publications:
            header_item = item.header
            # print(eeke)
            if header_item.startswith("Note"):
                city_name = item.city
                text_tweet = item.text
                publication_date = item.date
                publication_header = item.header
                with open(mypath, "a") as a_file:
                    a_file.write(f'{publication_header}')
                    a_file.write(f'{text_tweet}\n')  
                    a_file.write(f'{city_name}, ')
                    a_file.write(f'{publication_date}\n')       
                    a_file.write("\n")
                    
            if header_item.startswith("Joke"):
                city_name = item.city
                text_tweet = item.text
                publication_date = item.date
                publication_header = item.header
                with open(mypath, "a") as a_file:
                    a_file.write(f'{publication_header}')
                    a_file.write(f'{city_name}\n')
                    a_file.write(f'{text_tweet}\n')
                    a_file.write(f'{publication_date}\n')       
                    a_file.write("\n")
                    
            if header_item.startswith("Confidential"):
                city_name = item.city
                text_tweet = item.text
                publication_date = item.date
                publication_header = item.header
                date_1 = dt.strptime(publication_date, "%d/%m/%Y %H.%M")                        
                end_date = f'{(date_1 + td(days=item.daysleft)).strftime("%d/%m/%Y")}'
                day_ending = "day" if item.daysleft == 1 else "days"       
                with open(mypath, "a") as a_file:
                    a_file.write(f'{publication_header}')
                    a_file.write(f'{text_tweet}\nActual until: {end_date}, {item.daysleft} {day_ending} left\n' )