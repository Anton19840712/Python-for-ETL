# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 13:55:14 2021

@author: User
"""


# def boolean_duplicates (*args):
#     list_of_args = []    
#     for i in args:
#         list_of_args.append(i)
#     a_set = set(list_of_args)
#     contains_duplicates = len(list_of_args) != len(a_set)
#     return contains_duplicates

# #Main area:    
# contains_dupes = boolean_duplicates(1,3,4,4)
# print(contains_dupes)


def calculate_averages():    
    list_of_numbers = [1, 2, 3, 4, 5]
    window_size = 3
    cumulative_sum = [0]
    moving_frames = []
    
    for i, x in enumerate(list_of_numbers, 1):
        cumulative_sum.append(cumulative_sum[i-1] + x)
        if i>=window_size:
            moving_frame = (cumulative_sum[i] - cumulative_sum[i-window_size])/window_size
            moving_frames.append(moving_frame)    
    return moving_frames

moving_average_results = calculate_averages()
for i in moving_average_results:
    print(i)