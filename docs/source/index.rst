Welcome to Corpora's documentation!
===================================
Corpora is a lightweight raw text corpus system able to store a collection of raw text documents with additional key-value headers. Text headers element is basically a python dict object that can store any kind of yaml serializable data as a values and strings as keywords.

Corpora provides four main features:
  * create a new corpus,
  * append document to a corpus,
  * random access to any document in a corpus by it's unique ``id``,
  * sequential access (generator over collection).

An action of modifying documents in a corpora is not available as this system ment to be KISS and supports only append & read-only.

A single corpus is represented as a directory in the filesystem, containing corpus chunk files, a config file, and index files. Corpora supports corpus file chunking, what make it possible to use it with no limit corpus size.

Corpus chunks (storing raw text & headers) are human readable (but not editable due to index design).

Quickstart
----------
Installation:
::
    
    > sudo pip install corpora

Basic usage:

    >>> from corpora import Corpus
    >>> Corpus.create('/tmp/test_corpus')
    >>> c = Corpus('/tmp/test_corpus')
    >>> c.add('First document', 1)
    >>> c.add('Second document', 2)
    >>> c.save_indexes()
    >>> len(c)
    2
    >>> c[1]
    ({'id': 1}, u'First document')
    >>> c[2]
    ({'id': 2}, u'Second document')
    >>> for t in c:
    ...    print t
    ... 
    ({'id': 1}, u'First document')
    ({'id': 2}, u'Second document')

Contents
========
.. toctree::
   :maxdepth: 2
   
   motivation
   api
   corpus
   benchmarks
   credits



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

