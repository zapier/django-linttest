import os
import sys
import unittest
import re
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class DjangoLinttestTest(unittest.TestCase):
    def test_generates_lint_tests_for_project(self):
        from linttest.base import LintBaseTestCase

        class ExampleProjectLintTest(LintBaseTestCase):
            excludes = []
            project_dir = './tests/example_project'
            since_commit = '85b87f9c65fa53c346cd0760c2261ad85291d709'

        lint_tester = ExampleProjectLintTest
        self.assertIn(
            'test_lint_tests_example_project_polls_models_py',
            lint_tester.__dict__
        )
        self.assertTrue(True)
