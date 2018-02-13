from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='Python-MS-SDK',
    version='0.8.1',
    packages=find_packages(),
    description='Repo: https://github.com/SphereMall/Python-MS-SDK',
    author='Kravets Roman',
    author_email='r.kravets@spheremall.com',
    install_requires=[
        'requests==2.18.4'
    ],
    url='https://github.com/SphereMall/Python-MS-SDK/wiki',
)