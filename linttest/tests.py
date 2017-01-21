from django.conf import settings
from django.test import TestCase
from linttest.base import LintBaseTestCase


EXCLUDES = getattr(settings, 'LINT_TEST_EXCLUDES', [])
PROJECT_DIR = getattr(settings, 'LINT_TEST_PROJECT_DIR', getattr(settings, 'BASE_DIR'))
SINCE_COMMIT = getattr(settings, 'LINT_TEST_SINCE_COMMIT')

if not PROJECT_DIR:
    import warnings
    warnings.warn("You haven't specified a project directory for lint testing!")

if not SINCE_COMMIT:
    import warnings
    warnings.warn("You haven't specified a commit to use as a base for lint testing!")


class LintTestCase(LintBaseTestCase, TestCase):
    excludes = EXCLUDES
    project_dir = PROJECT_DIR
    since_commit = SINCE_COMMIT
