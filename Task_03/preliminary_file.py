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

def sort_my_random_list(randomList:list):#fucntion sorts initial random list with values    
    sorted_randomlist = []#creates empty list    
    while randomList:#then go throw it        
        minimum = randomList[0]#takes first value as initial point of calculations         
        for x in randomList:#compares each value with the next one in a loop and find the smallest value among all the others values           
            if x < minimum: #and if detects it, it:               
                minimum = x #writes it in a variable so called "minimum" as a new minimum        
        sorted_randomlist.append(minimum)#and then adds it to a new given list        
        randomList.remove(minimum) #also removes minimum we found from our list, just not to loop again it the next iteration    
    return sorted_randomlist #and returns our sorted list as result

def calculate_average_odd_and_even(initial_list:list):#complex function, need refactoring to be simplified, calculates logic for odd and even numbers in list    
    odd_counter, even_counter, odd_sum, even_sum = 0, 0, 0, 0 #declaration of variables 
    for num in initial_list:#function enables to loop throw list in for cycle:        
        if (num % 2) == 0:#if this is an odd value in a list:           
            odd_sum = odd_sum + num #we sum it with current sum value            
            odd_counter = odd_counter + 1 #and also increment an odd counter            
        else:#else we            
            even_sum = even_sum + num #do the same with even numbers            
            even_counter = even_counter + 1 #increasing even_counter variable 
    try:#here function pass execution to calculate_average function: add checking of generated values by EAFP principle: easier to ask for forgivness, than permission...
        odd_average  = calculate_average(odd_sum, odd_counter)
    except ValueError:
        print("Oops!  There were no odd numbers in collection...")    
    if even_counter > 0: #here we calculate average using parameters: add checking of generated values by LBYL principle: loop before you leap. But could use EAFP instead.
        even_average = calculate_average(even_sum, even_counter)
    else:
        print("Oops!  There were no even numbers in collection...")    
    print_calculate_average(round(odd_average,6), "odd_values_average")#here we print average results using parameters    
    print_calculate_average(round(even_average,5), "even_values_average") #here we print average results using parameters    

def calculate_average(summa:int, counter:int):#function, that calculates average values for odd and even numbers    
    average_calculated = summa/counter#by dividing sum value by its counter value    
    return average_calculated#and returns result back

def print_calculate_average(print_list:list, label:int):#functions prints average results    
    print(f"{label}: {print_list}")#use parameters in string

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
sorted_list = sort_my_random_list(numbers)#new variable sorted_list, that gets result of calculations of function
for count, i in enumerate(sorted_list, 1):#loop prints number of the current element    
    print(count, i)#ptints for each iteration
print("\nAverage of odd and even values:") #prints header
print("-------------------------------")
calculate_average_odd_and_even(sorted_list)#method calculates averages for odd and even values of the list