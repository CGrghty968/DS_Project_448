"""
@author : Cillian Geraghty
@version : 1.0.0
"""

import re

def user_name(user_name):
    """
    
    :param user_name: 
        String, the user's username
    :return: 
        String, the user's confirmed username
    """

    pattern = r'^[a-zA-Z0-9_,.\'-]{5,50}$'

    if re.match(pattern, user_name):
        return "Username: "+user_name
    else:
        return "Invalid Username"

def user_score(user_score, update):
    """

    :param user_score:
        Integer, the user's score
    :param update:
        Integer, the user's update amount
    :return:
        Integer, the updated user score
    """
    if not isinstance(user_score, int) or not isinstance(update, int):
        return "Invalid input! Please enter a valid integer."

    return user_score + update

