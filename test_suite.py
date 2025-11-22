"""
@author: Cillian Geraghty
@version: 1.0.0
@file: test_suite.py
"""
import unittest

def run_test_suite():
    """
    Discover and run all tests in test_main.py in the same directory
    """

    # Discover tests in test_main.py in the same directory
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="./", pattern='test_main.py')

    # Run the tests with verbose output of 2
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Return the result for further processing if needed
    return result


if __name__ == '__main__':
    run_test_suite()
