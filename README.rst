Django Lint Test
================

Lint Test is a simple Django app to perform flake8 linting on your
project. You'll set a settings.LINT\_TEST\_SINCE\_COMMIT from some
commit in your git history.

It will then check files changed since that commit origin and ensure
they lint properly. If any file doesn't lint properly your unit test run
will fail.

## Quick start
--------------

1. ``pip install linttest``

2. Add "linttest" to your INSTALLED\_APPS setting like this::

   ::

           INSTALLED_APPS = [
               ...
           'linttest',
           ]

3. Specify the commit origin in your settings (sh> git log)::

   ::

           LINT_TEST_SINCE_COMMIT = '<commit hash>'

4. Run the management command::

   ::

           python manage.py linttest

           or

           python manage.py test linttest

5. Fix any files that fail the linting!

## Run with your normal tests suite
-----------------------------------

1. Verify installation with the "Quick Start" guide

2. Add a test that extends the ``LintTestCase`` to another test file in
   your project

   ::

           from linttest.tests import LintTestCase


           class MyLintTests(LintTestCase):
               pass

3. Run the test command::

   ::

           python manage.py test

This is required for django 1.6 and up because the DiscoveryRunner
defaults to just running tests in your project.

For local installation
----------------------

1. Git clone...

2. Package it

   ::

           python setup.py sdist  # rerun this and the next step on change

3. From your desired install project - note the relative path - update
   for your project location

   ::

           pip install ../linttest/dist/linttest-0.1.tar.gz

   or

   ::

           pip install ../linttest/dist/linttest-0.1.tar.gz --upgrade  # rerun on change

4. You can follow the quickstart from there
