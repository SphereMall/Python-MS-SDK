from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='Python-MS-SDK',
    version='1.0',
    packages=find_packages(),
    author='Kravets Roman',
    author_email='r.kravets@spheremall.com',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)