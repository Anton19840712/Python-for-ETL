# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:36:08 2021

@author: User
"""
from publisher import*

class Human:
    def __init__(self, age):
        self.age = age
        
class Author(Human):
    def __init__(self, name, **mydict):
        super().__init__(**mydict)
        self.name = name
        
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
    def add_publication(self, publication, mypath):
        self.counter = self.counter + 1
        if len(self.publications) < self.max_number_of_publications:
            self.publications.append(publication)
            ptype = publication.publicationtype
            if ptype == "note":
                publication.header = "Note-------------------------\n"
                note_publisher = NotePublisher()
                context = Publisher(note_publisher)
                context.context_interface(publication, mypath)
            if ptype == "joke":
                publication.header = "Joke of the day--------------\n"
                joke_publisher = JokePublisher()
                context = Publisher(joke_publisher)
                context.context_interface(publication, mypath)
            if ptype == "confidential":
                publication.header = "Confidential tweet-----------\n"
                confidential_publisher = ConfidentialPublisher()
                context = Publisher(confidential_publisher)
                context.context_interface(publication, mypath)
            return True
        else:
            print(f"You publication number {self.counter} in aborted!")
            return False