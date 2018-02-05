# coding=utf-8

import unittest
import sys,os

from Environment import environment

def _run_suite(suite):
    '''
    :param suite: run tests from a unittest.TestSuite-derived class
    :return: 
    '''
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        if len(result.errors) == 1 and not result.failures:
            err = result.errors[0][1]
        elif len(result.failures) == 1 and not result.errors:
            err = result.failures[0][1]
        else:
            err = "multiple errors occured"
            raise Exception(err)

def run_unittest(classes):
    '''
    :param classes: run tests from unittest.TestCase-derived-= classes
    :return: 
    '''
    valid_types = (unittest.TestSuite, unittest.TestCase)
    suite = unittest.TestSuite()
    for cls in classes:
        if isinstance(cls, str):
            if cls in sys.modules:
                suite.addTest(unittest.findTestCases(sys.modules[cls]))
            else:
                raise ValueError("str arguments must be keys in sys.modules")
        elif isinstance(cls, valid_types):
            suite.addTest(cls)
        else:
            suite.addTest(unittest.makeSuite(cls))
    _run_suite(suite)

# add new testcases here
from testcase.common.utils.Test_JsonUtil import Test_JsonUtil

if __name__ == "__main__":
    run_unittest([
        Test_JsonUtil,
    ])