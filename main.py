"""
@author : Cillian Geraghty
@file   : main.py
@version : 2.0.0
"""

import logging
import re

"""
Basic Logger for the system
"""
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def user_name(name):
    """
    :param name:
        String, the user's username
    :return:
        String, the user's confirmed username
    """

    logger.debug(f"Validating username: %s", name)

    pattern = r'^[a-zA-Z0-9_,.\'-]{5,50}$'

    if re.match(pattern, name):
        logger.info(f"Valid username received: %s", name)
        return "Username: " + name

    logger.warning(f"Invalid username input: %s", name)
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

    logger.debug(f"Updating user score: score=%s, update=%s", score, update)

    if not isinstance(score, int) or not isinstance(update, int):
        logger.error("Invalid input types for score or update")
        return "Invalid input! Please enter a valid integer."

    new_score = score + update
    logger.info(f"Score updated successfully: new_score=%s", new_score)
    return new_score
