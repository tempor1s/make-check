from setuptools import setup, find_packages

description = """
See `github repo <https://github.com/tempor1s/make-checkin>`_ for information.
"""

VERSION = '1.0.4'  # maintained by release tool


setup(
    name='Make Checkin',
    version=VERSION,
    author='Ben Lafferty',
    author_email='benlaugherty@gmail.com',
    entry_points={
        'console_scripts': ['checkin=checkin.command_line:main']
    },
    description='A CLI application that allows you to checkin to a MakeSchool class.'
)