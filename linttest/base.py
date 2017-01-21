"""

"""

import unittest
from git import Repo
from pep8 import StandardReport
from flake8.api import legacy as flake8
import os
import fnmatch


class NoPrintReport(StandardReport):
    def get_file_results(self):
        if self.counters['files'] == 0:
            # File must of had a file-level noqa
            return ''

        self._deferred_print.sort()
        results = ''

        for line_number, offset, code, text, doc in self._deferred_print:
            results += '{path}:{row}:{col}: {code} {text}\n'.format(
                path=self.filename,
                row=self.line_offset + line_number,
                col=offset + 1,
                code=code,
                text=text
            )

        return results.strip()


def make_test(file_path, project_dir):
    """ Generate a test method """
    def run(self):
        # jobs='1' or else flake8 goes nuts on reporter
        flake8_style = flake8.get_style_guide(
            config_file=os.path.join(project_dir, '.flake8'), max_complexity=-1,
            jobs='1', reporter=NoPrintReport)
        report = flake8_style.input_file(file_path)
        text_results = '\n'.join(report.get_statistics('E') + report.get_statistics('W'))
        self.assertEquals('', text_results, 'linting failed for {}:\n\n{}'.format(
            file_path.replace(project_dir + '/', ''), text_results))
    return run


class LintBuildTestCase(type):
    def __new__(cls, name, bases, attrs):
        excludes = attrs.get('excludes', [])
        project_dir = attrs.get('project_dir', './')
        since_commit = attrs.get('since_commit', '')
        repo = Repo(project_dir)
        changed_file_paths = set(
            os.path.join(project_dir, d.b_path)
            for d in repo.commit(since_commit).diff(None)
        )

        file_paths = set()
        for dirpath, dnames, fnames in os.walk(project_dir):
            for fname in fnames:
                file_path = os.path.join(dirpath, fname)

                is_python = file_path.endswith('.py')
                is_changed = file_path in changed_file_paths
                isnt_excluded = not any(fnmatch.fnmatch(file_path, e) for e in excludes)
                if is_python and is_changed and isnt_excluded:
                    file_paths.add(file_path)
        for file_path in file_paths:
            file_path_clean = file_path.replace('/', '_').replace('.', '_').strip('_')
            test = make_test(file_path, project_dir)
            test.__name__ = name
            test.__doc__ = '%s => linted!!!' % (file_path_clean)
            test_name = 'test_lint_{}'.format(file_path_clean)
            attrs[test_name] = test

        return super(LintBuildTestCase, cls).__new__(cls, name, bases, attrs)


class LintBaseTestCase(unittest.TestCase):
    __metaclass__ = LintBuildTestCase
    excludes = []
    project_dir = './'
    since_commit = ''
