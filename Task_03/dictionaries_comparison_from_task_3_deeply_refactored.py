# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:18:07 2021

@author: User
"""
import numpy as np
import string

#Functions:
def set_random_array_for_fixed_random():
    #just not to have random in random) I decided to use seed and set_state
    np.random.seed(1234) #we throw in seed 1234 and get from it state based on the first random number from generator of pseudo-random sequence
    state = np.random.get_state() # get generation results
    print(f'this is state {state}')
    np.random.set_state(state)    ### very useful staff for repeatability of experiments make it stable in memory


def set_random_number_of_lists():
    n = np.random.randint(2,10,1)[0] #then we take first random) value from array
    print(f'it was {n}')
    list_dicts = [None]*n #allocating n number of lists
    for i in range(len(list_dicts)): # for each item in list create accordingly to this number a number of items
        list_dicts[i] = dict(zip(np.random.choice(list(string.ascii_letters),3),np.random.randint(1,100,3))) #generate dictionary we glue here our key and value
    for i in list_dicts:
        print(i)
    return list_dicts

def unite_dictionaries_by_unique_keys(list_dicts:list):
    #set lits for dictionary keys
    all_k = []
    #set lits for dictionary values
    all_v = []
    #foreach pair in dictionary get keys in list
    for i in list_dicts:
        for k in i.keys():
            all_k.append(k)
            # get values in list
        for v in i.values():
            all_v.append(v)
    #then get all unique keys
    uniq_k = np.unique(all_k)
    #allocating new common dictionary
    res_dict = {}
    #then run by unique keys
    for i in uniq_k:
        #setting initial max value to escape if number in real dictionary could be bigger
        max_val = -1
        #getting current key from i
        res_key = i
        #declaring counter
        counter = 0
        #then we loop over each key from all keys collection
        for j, k in enumerate(all_k):
            # if key == key compare key from unique key collection and common key collection
            # if match
            if (i == k):
                #and if value by the key > than -1
                if (max_val<all_v[j]):
                    # we get it
                    max_val=all_v[j]
                    #increase our counter
                    counter+=1
                    if (counter>1):
                        #renaming key
                        res_key=f'{i}_{counter}'  
        #setting max value by this renamed key to dictionary
        res_dict[res_key] = max_val
    print(res_dict)

#Main area:
set_random_array_for_fixed_random()
list_dicts = set_random_number_of_lists()
unite_dictionaries_by_unique_keys(list_dicts)



