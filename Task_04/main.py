# -*- coding: utf-8 -*-
""" 
Created on Fri Mar 26 22:04:14 2021
@author: User
"""
from publication import *
from human import *
from reader import *

from publisher_manager import * 
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
    def __init__(self, age, name, max_number = 3):
        self.max_number_of_publications = max_number
        self.publications = []
        super().__init__(age=age, name=name)
    def __repr__(self):
        return "name: {}, age: {}, max_number_of_publications: {}".format(
                self.age, 
                self.name, 
                self.max_number_of_publications)    
    def add_publication(self, publication):
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
            print("Too much publications, man...! Pay me money, I am tired)")
            return False
    # when we want to dump the data from memory to file 
    def dump_publications(self):
        dump_publisher = DumpPublisher()
        context = PublisherManager(dump_publisher)
        context.context_interface(self.publications)
    # when we want to parse the data from file to memory    
    def parse_to_list_publications(self):
        text = ContentReader.read_from_file()
        notes = ContentReader.read(text)
        print("Reading from files results:\n\n****************************\n")
        try:
            for i in notes:
                print(f'{i.header}\n{i.text_second_row}\n{i.text_third_row}\n{i.text_fourth_row}\n')
        except TypeError:
            print("Object is not iterable")
        except:
            print("Unexpected error:", sys.exc_info()[0])


#Test area:
def main():
    n1 = Publication("note", "London", "Hello, world" )
    n2 = Publication("joke", "Moscow", "Hello, world")
    n3 = Publication("confidential", "Minsk", "Hello, world", 21)
    n4 = Publication("note", "New_York", "Hello, world")
    
    user = User("Anton", 34)
    
    user.add_publication(n1)
    user.add_publication(n2)
    user.add_publication(n3)
    user.add_publication(n4)
    
if __name__ == "__main__":
    main()

# user.dump_publications()
# user.parse_to_list_publications()