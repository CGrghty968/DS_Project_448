import unittest
from unittest import TestCase
from main import user_name, user_score

class TestUserName(TestCase):

    def test_valid_user_name(self):
        """
        Function to test the user_name validator function, using valid usernames
        """
        valid_names = ["john123", "user_name", "test.user", "abcde", "a" * 50]
        for name in valid_names:
            self.assertEqual(user_name(name), f"Username: {name}")

    def test_invalid_usernames(self):
        """
        Function to test the use_name validator function, using invalid usernames
        """
        invalid_names = ["abcd", "a" * 51, "user@name", "user name", ""]
        for name in invalid_names:
            self.assertEqual(user_name(name), "Invalid Username")

class TestUserScore(TestCase):

    def test_valid_score_updates(self):
        """
        Function to test the valid score update values
        """
        # Testing the positive update values
        self.assertEqual(user_score(100, 50), 150)
        self.assertEqual(user_score(0, 10), 10)

        # Testing the negative update values
        self.assertEqual(user_score(100, -25), 75)
        self.assertEqual(user_score(50, -10), 40)

        # Testing zero update
        self.assertEqual(user_score(100, 0), 100)

    def test_type_error_handling(self):
        """
        Function for testing the error handling in the user_score function
        """



        self.assertEqual(user_score("1e0", 50), "Invalid input! Please enter a valid integer.")
        self.assertEqual(user_score(100, "5a0"), "Invalid input! Please enter a valid integer.")
        self.assertEqual(user_score("abc", "xyz"), "Invalid input! Please enter a valid integer.")


# def suite():
#     test_suite = unittest.TestSuite()
#     test_suite.addTest(unittest.makeSuite(TestUserScore))
#     test_suite.addTest(unittest.makeSuite(TestUserName))
#
#     return test_suite
#
# mySuite = suite()
# runner = unittest.TextTestRunner()
# runner.run(mySuite)