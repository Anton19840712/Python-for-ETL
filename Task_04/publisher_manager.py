# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 22:54:01 2021

@author: User
"""
from datetime import timedelta as td
from datetime import datetime as dt
import abc
 
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