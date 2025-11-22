"""
@author : Cillian Geraghty
@file   : main.py
@version : 1.0.0
"""

import re

def user_name(name):
    """
    
    :param name: 
        String, the user's username
    :return: 
        String, the user's confirmed username
    """

    pattern = r'^[a-zA-Z0-9_,.\'-]{5,50}$'

    if re.match(pattern, name):
        return "Username: "+name

    return "Invalid Username"

def user_score(score, update):
    """

    :param score:
        Integer, the user's score
    :param update:
        Integer, the user's update amount
    :return:
        Integer, the updated user score
    """
    if not isinstance(score, int) or not isinstance(update, int):
        return "Invalid input! Please enter a valid integer."

    return score + update
