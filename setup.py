# from distutils.core import setup
from setuptools import setup

setup(
    name='Corpora',
    version='1.0',
    author="Krzysztof Dorosz",
    author_email="cypreess@gmail.com",
    description=("Lightweight, fast and scalable text corpus library."),
    license="LGPL",
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
    requires=['pyyaml', 'bsddb3'],

 )