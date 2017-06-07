import os
import sys
import unittest
import re

import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class DjangoLinttestTest(unittest.TestCase):
    def test_generates_lint_tests_for_project(self):
        # self.getProject()
        # run linttest get_tests on project??
        self.assertTrue(True)
