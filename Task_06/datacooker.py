# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:33:59 2021

@author: User
"""
import re

class DataCooker():
    def cook_me_data(my_data:str):
        new_str = re.sub('[^a-zA-Z\.]', ' ', my_data)
        newstring = new_str.replace('.', ' ')
        return newstring
    def lower_case_me_string(newstring:str):        
        lowercase_string = newstring.lower()
        return lowercase_string
    def cut_whitesapces(char_pieces:dict):
        cleaned_from_whitespaces = {k: v for k, v in list(char_pieces.items()) if k != " "}
        return cleaned_from_whitespaces
    def count_upper_chars(new_data:list):
        counter_upper = 0;
        for k, v in new_data.items():
            if str(k).isupper():
                counter_upper = counter_upper + 1
        return counter_upper
    def sort_me_list(new_data:list):
        char_list = {k: v for k, v in sorted(new_data.items(), key=lambda item: item[1])}
        return char_list
    def count_sum_of_values(char_list:list):
        sum_of_values = sum(char_list.values())
        return sum_of_values
    def sort_spinach(counted_list:list):
        sorted_list = {k: v for k, v in sorted(counted_list.items(), key=lambda item: item[1])}
        return sorted_list