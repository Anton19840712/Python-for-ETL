# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:14:52 2021

@author: User
"""

import random
import string
import re


def generate_random_value_for_number_of_dicts():
    n = random.randint(2, 10)
    return n

def generate_random_letter_key_for_dict():
    n = random.choice(string.ascii_letters)
    return n

def generate_random_number_value_for_dict():
    n = random.randint(0, 100)
    return n

def generate_template_dict():
    n = generate_random_value_for_number_of_dicts()    
    dict_template = {}    
    for i in range(0, n):
        letter_key = generate_random_letter_key_for_dict()
        number_value = generate_random_number_value_for_dict()        
        dict_template[letter_key] = number_value        
    return dict_template

def generate_dicts_for_list(n:int):    
    list_of_dicts = []    
    for i in range(0, n):
        dict_sample = generate_template_dict()        
        list_of_dicts.append(dict_sample)        
    return list_of_dicts

def merge_dicts_by_keys(full_list:list):       
    created_list = create_appended_list(full_list)    
    created_list = sort_my_list(created_list)        
    rewrite_elements(created_list)                    
    created_list = sort_my_list(created_list)    
    dct = dict([ (re.split(r"[:_]", s)[0], s) for s in created_list])
    lst_uniq = list(dct.values())      
    dict_final_result = {}     
    dict_final_result = {x.split(':')[0]:int(x.split(':')[1]) for x in lst_uniq}    
    return dict_final_result  


def create_appended_list(full_list:list):
    appended_list = []
    for idict in full_list:
        for o in idict:
            appended_list.append(f"{o}:{idict[o]}")
    return appended_list


def rewrite_elements(created_list:list):
    counter = 0
    for i in range(len(created_list)):
        elements_1 = created_list[i].split(":") 
        formal_k_1 = elements_1[0]
        formal_v_1 = elements_1[1]        
        for j in range(i + 1, len(created_list)):            
            elements_2 = created_list[j].split(":")
            formal_k_2 = elements_2[0]
            formal_v_2 = elements_2[1]
            if formal_k_1 is formal_k_2:
                if formal_v_1 < formal_v_2:
                    counter = counter + 1
                    created_list[j] = f"{formal_k_2}_{counter}:{formal_v_2}"
                    

def sort_my_list(mylist:list):
    mylist.sort()
    return mylist

#Main area:
number_of_dicts = generate_random_value_for_number_of_dicts()
list_of_dicts = generate_dicts_for_list(number_of_dicts)
for i in list_of_dicts:    
    print(i)    
compared_united_list_of_dicts = merge_dicts_by_keys(list_of_dicts)
print("----------")
for i in compared_united_list_of_dicts:
    print (i, compared_united_list_of_dicts[i])

    

    
    

