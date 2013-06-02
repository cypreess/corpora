# from distutils.core import setup
from setuptools import setup

setup(
    name='Corpora',
    version='1.1',
    author="Krzysztof Dorosz",
    author_email="cypreess@gmail.com",
    description="Lightweight NLP corpus format for python",
    license="MIT",
    keywords="text utf corpus corpora nlp toolkit",
    packages=['corpora', 'test'],
    long_description=open('README.rst').read(),
    url="https://github.com/cypreess/corpora/",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Topic :: Utilities",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Text Processing",

    ],
    install_requires=['pyyaml', 'bsddb3'],

 )