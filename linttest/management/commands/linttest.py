from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Run the linting tests'

    def handle(self, *args, **options):
        call_command('test', 'linttest.tests.LintTestCase', **options)
