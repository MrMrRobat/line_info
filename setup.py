import ast
import io
import os
import re

from pkg_resources import parse_requirements
from setuptools import setup

CURDIR = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, 'README.md'), 'r', encoding='utf-8') as f:
    README = f.read()

with open(os.path.join(CURDIR, 'requirements.txt'), 'r', encoding='utf-8') as f:
    REQUIREMENTS = f.read()


def get_version():
    init_path = os.path.join(CURDIR, 'line_info', '__init__.py')
    with open(init_path, 'r', encoding='utf8') as init:
        match = re.search(r'__version__\s+=\s+(?P<version>.*)', init.read())
        version = match.group('version') if match is not None else "'unknown'"
    return str(ast.literal_eval(version))


setup(
    name='line_info',
    version=get_version(),
    author='MrMrRobat',
    author_email='appkiller16@gmail.com',
    description='CLI tool to fetch helpful info about line of code, such as issue number, related PRs, etc.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/MrMrRobat/line_info',
    packages=['line_info'],
    include_package_data=True,
    entry_points={'console_scripts': ['line_info=line_info.__main__:main']},
    zip_safe=False,
    install_requires=map(str, parse_requirements(REQUIREMENTS)),
    python_requires='>=3.6',
    license='License :: OSI Approved :: MIT License',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)