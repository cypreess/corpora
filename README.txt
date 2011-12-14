Welcome to Corpora!
===================
*Corpora* is a lightweight, fast and scalable corpus library able to store a collection of raw text documents with additional key-value headers. It uses Berkeley DB (bsddb3 module) for index managing what guarantee speed and bullet-proof. Text storage model is based on chunked flat, human readable text files. This architecture can easily scale up to millions documents, hundred of gigabytes collections.

Corpora module provides four main features:
  * create a new corpus,
  * append documents to a corpus,
  * random access to any document in a corpus using it's unique ``id``,
  * sequential access to document collection (generator over collection).

Key-Value document headers supports storing any kind of objects seriazable with yaml_. Corpora supports only append & read-only philosophy, for more information please read section :doc:`motivation`.

.. _yaml: http://www.yaml.org/

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