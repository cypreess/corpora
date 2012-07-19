# from distutils.core import setup
from setuptools import setup

setup(
    name='Corpora',
    version='1.1',
    author="Krzysztof Dorosz",
    author_email="cypreess@gmail.com",
    description=("Lightweight NLP corpus format for python"),
    license="MIT",
    keywords="text utf corpus corpora nlp toolkit",
    packages=['corpora', 'test'],
    long_description=open('README.txt').read(),
    url="http://packages.python.org/corpora",
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Text Processing",

    ],
    install_requires=['pyyaml', 'bsddb3'],

 )