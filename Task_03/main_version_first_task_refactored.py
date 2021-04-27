# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random # import library random

#Functions block
#===============
def create_list_with_random_values(): #function calls function for random values generation and returns list    
    random_list = [random.randint(0, 1000) for i in range(100)] # creating random list    
    return random_list

def calculate_average_odd_and_even(initial_list:list):#calculates logic for odd and even numbers in list
    try:  
        list_odds_average = sum(list(filter(lambda x: x%2 == 1, initial_list)))/len(list(filter(lambda x: x%2 == 1, initial_list)))
    except ValueError:
        print("Oops!  There were no odd numbers in collection...")
    finally:
        print(round(list_odds_average,6), "odd_values_average") #here we print average results using parameters   
    try:     
        list_even_average = sum(list(filter(lambda x : x%2 == 0, initial_list)))/ len(list(filter(lambda x : x%2 == 0, initial_list)))
    except ValueError:
        print("Oops!  There were no even numbers in collection...")
    finally:
        print(round(list_even_average,6), "even_values_average") #here we print average results using parameters  

def insertion_sort(arr):        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i        
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor
    return arr

#Main block
#==========
print("\nRandom unsorted:")# print words "Random unsorted"
print("----------------")
numbers = create_list_with_random_values()#variable, that gets result of calculations of function
for count, i in enumerate(numbers, 1):
    print(count, i)
print("-----------")
number_of_elements = len(numbers)#gettin length of list
print(f"Count: {number_of_elements}")
print("\nRandom sorted:")
print("--------------")
sorted_list =  insertion_sort(numbers)#new variable sorted_list, that gets result of calculations of function
counter = 0
for count, i in enumerate(sorted_list, 1):#loop prints number of the current element    
    print(count, i)#ptints for each iteration
print("\nAverage of odd and even values:") #prints header
print("-------------------------------")
calculate_average_odd_and_even(numbers)#method calculates averages for odd and even values of the list