#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Deepak Tatyaji Ahire",
    author_email='ahiredeepak20@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Solutions to all the assignments for STEPIK interactive text",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='coursera_bioinformatics_specialization_solutions, finding_hidden_messages_in_dna',
    name='coursera_bioinformatics_specialization_solutions',
    packages=find_packages(include=['coursera_bioinformatics_specialization_solutions', 'coursera_bioinformatics_specialization_solutions.*', 'finding_hidden_messages_in_dna', 'finding_hidden_messages_in_dna.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/adeepak7/finding_hidden_messages_in_dna',
    version='0.1.0',
    zip_safe=False,
)
