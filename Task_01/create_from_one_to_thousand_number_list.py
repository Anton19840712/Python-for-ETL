# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Functions block

# import library random
import random

# function generates random value
def create_list_with_random_values(): #function calls function for random values generation and returns list    
    random_list = [random.randint(0, 1000) for i in range(100)] # creating random list    
    return random_list

#fucntion sorts initial random list with values
def sort_my_random_list(randomList:list):
    #creates empty list
    sorted_randomlist = []
    #then go throw it
    while randomList:
        #takes first value as initial point of calculations 
        minimum = randomList[0]
        #compares each value with the next one in a loop and find the smallest value among all the others values
        for x in randomList:
            #and if detects it, it:
            if x < minimum:
                #writes it in a variable so called "minimum" as a new minimum
                minimum = x
        #and then adds it to a new given list
        sorted_randomlist.append(minimum)
        #also removes minimum we found from our list, just not to loop again it the next iteration
        randomList.remove(minimum) 
    #and returns our sorted list as result
    return sorted_randomlist

#complex function, need refactoring to be simplified, calculates logic for odd and even numbers in list
def calculate_average_odd_and_even(initial_list:list):
    #declaring of an odd_counter variable
    odd_counter = 0
    #declaring of an even_counter variable 
    even_counter = 0
    #assigning of odd_sum variable 
    odd_sum = 0
    #declaring of an even_sum variable 
    even_sum = 0
    #function enables to loop throw list in for cycle:
    for num in initial_list:
        #if this is an odd value in a list:
        if (num % 2) != 0:
            #we sum it with current sum value
            odd_sum = odd_sum + num
            #and also increment an odd counter
            odd_counter = odd_counter + 1
            #else we
        else:
            #do the same with even numbers
            even_sum = even_sum + num
            #increasing even_counter variable
            even_counter = even_counter + 1
    #here function pass execution to calculate_average function:
    try: 
        odd_average  = calculate_average(odd_sum, 0)
    except ZeroDivisionError:
        print("Oops! Division by zero exception!")      
    finally:
        even_average = calculate_average(even_sum, even_counter)
            
    #here we print average results using parameters
    try:
        print_calculate_average(round(odd_average,6), "odd_values_average")
    except UnboundLocalError: 
        print("Something went wrong with calculations of odds. See information above ↑")
    ##here we print average results using parameters
    try:
        print_calculate_average(round(even_average,5), "even_values_average") 
    except UnboundLocalError: 
        print("Something went wrong with calculations of even numbers. See information above ↑")
#function, that calculates average values for odd and even numbers
def calculate_average(summa:int, counter:int):
    #by dividing sum value by its counter value
    average_calculated = summa/counter
    #and returns result back
    return average_calculated

#functions prints average results
def print_calculate_average(print_list:list, label:int):
    #use parameters in string
    print(f"{label}: {print_list}")


# Main block
# print words "Random unsorted"
print("\nRandom unsorted:")
#print string "----------------"
print("----------------")
#variable, that gets result of calculations of function
numbers = create_list_with_random_values()
#
for count, i in enumerate(numbers, 1):
    #
    print(count, i)
    
# prints string like "-----------"
print("-----------")
#gettin length of list
number_of_elements = len(numbers)
#print number of elements in this list
print(f"Count: {number_of_elements}")
#prints header
print("\nRandom sorted:")
#prints header
print("--------------")
#new variable sorted_list, that gets result of calculations of function
sorted_list = sort_my_random_list(numbers)
#loop prints number of the current element
for count, i in enumerate(sorted_list, 1):
    #ptints for each iteration
    print(count, i)
#prints header
print("\nAverage of odd and even values:") 
#prints header
print("-------------------------------")
#method calculates averages for odd and even values of the list
calculate_average_odd_and_even(sorted_list)