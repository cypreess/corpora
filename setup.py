# from distutils.core import setup
from setuptools import setup

setup(
    name='corpora',
    version='0.1',
    author="Krzysztof Dorosz",
    author_email="cypreess@gmail.com",
    description=("Lightweight raw text corpora system."),
    license="LGPL",
    keywords="text utf corpus corpora nlp toolkit",
    packages=['corpora', 'test'],
    long_description=open('README.txt').read(),
    # url="http://packages.python.org/pyhole",
    classifiers=[
        "Topic :: Utilities",
        # "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",

    ],
    requires=['pyyaml', ],

 )