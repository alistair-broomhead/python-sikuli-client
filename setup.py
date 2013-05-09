from setuptools import setup, find_packages
from os import path


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

setup(
    name='python-sikuli-client',
    include_package_data = True,
    package_data = {'':['*.md']},
    author='Alistair Broomhead',
    version='0.1.9',
    author_email='alistair.broomhead@gmail.com',
    description='Python library to act as a client for jython-sikuli-server',
    license='MIT',
    url='https://github.com/alistair-broomhead/python-sikuli-client',
    download_url='https://github.com/alistair-broomhead/python-sikuli-client/zipball/master',
    long_description=read('README.md'),
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    install_requires=['jython-sikuli-server']
)
