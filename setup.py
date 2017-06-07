import os
from setuptools import find_packages, setup

# with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
#     README = readme.read()

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='linttest',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'gitpython==2.1.1',
        'flake8==3.2.1',
        'pep8==1.7.0',
        'pyflakes==1.3.0'
    ],
    include_package_data=True,
    license='',
    test_suite='tests',
    description='A django lint test runner',
    url='https://github.com/zapier/django-linttest',
    download_url='https://github.com/zapier/django-linttest/tarball/0.1',
    author='Harrison Jackson',
    author_email='harrison.jackson@zapier.com',
    classifiers=[
        'Topic :: Software Development',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        # "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.3",
        # "Programming Language :: Python :: 3.4",
    ]
)
