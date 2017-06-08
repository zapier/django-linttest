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
            excludes = ['./tests/example_project/polls/views.py']
            lint_paths = ['./tests/example_project']
            project_dir = './'
            since_commit = '5573886a0aefa79ad29dc00706fcd20e3b1704a9'

        lint_tester = ExampleProjectLintTest
        self.assertIn(
            'test_lint_tests_example_project_polls_models_py',
            lint_tester.__dict__
        )
        self.assertNotIn('test_lint_tests_example_project_polls_views_py', lint_tester.__dict__)

        self.assertTrue(True)
