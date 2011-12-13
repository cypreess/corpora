Corpora API
===========
Corpora module is so far very simple and consists only of one class.

.. autoclass:: corpora.Corpus
    :members:

The only argument ``path`` should be pointed on directory containing corpus.

Creating new corpus
-------------------
To create new corpus use static method:

.. automethod:: corpora.Corpus.create

Example:
::
    
    Corpus.create('/tmp/test_corpus', name="My test corpus", chunk_size=1024*1024*10)

This will create an empty corpus with 10MB chunk size and name *My test corpus* in directory ``/tmp/test_corpus``.

Appending document to corpus
----------------------------

.. automethod:: corpora.Corpus.add

``text``
    a document raw text formed as an Unicode; this will be encoded with the ``encode`` property of corpus before saving to a chunk.
``ident``
    a unique identifier of an element, this can be a number or any string (ex. hash value); needed for random access.
``**headers``
    you can add any additional headers as key-value pairs; values can be any serializable by yaml objects; the key "id" is restricted for storing the document ident.
    
Example:
::
    
    c = Corpus('/tmp/test_corpus')
    c.add(u'This is some text', 1, fetched_from_url="http://some.test/place", related_documents=[1,2,3])
    c.add(u'Other text', 2, is_interesting=False)


.. note::

    documents are saved with order of appending them, this means that if you add 3 documents with ``id`` like 2, 1, 3 there will be served in the same order while accessed sequentially. 



.. warning::

    as you can see you can add any header to document. There is no pre-configuration what can be set as document header. This is very flexible, but in the same time can lead to problem with consistency of headers among all documents collections. Be sure that you append this same headers to every document in corpus or write your code in a way that will deal with ``KeyError`` from missing headers.

After adding new documents to a corpus you need to sync indexes to a filesystem.

.. automethod:: corpora.Corpus.save_indexes


::
    
    c.save_indexes()


Sequential access to corpus
---------------------------    
Typical use of a corpus is to sequentially access all documents one-by-one. Corpora supports operation with generators.

.. automethod:: corpora.Corpus.__iter__

Example:

::
    
    c = Corpus('/tmp/test_corpus')
    for (headers, text) in c:
        ... some processing

This will read a file chunks sequentially what should be as fast as possible.

Random access to corpus
-----------------------
There is also a possibility to access a given document pointed by it's ``id``. 

.. automethod:: corpora.Corpus.__getitem__

.. automethod:: corpora.Corpus.get

Examples:
::
    
    c = Corpus('/tmp/test_corpus')
    print c[1]
    print c.get(1)

Both lines will print the same document tuple (if exists).

Size of corpus
--------------
Standard python ``len`` is used.

.. automethod:: corpora.Corpus.__len__

Example:
::
    
    c = Corpus('/tmp/test_corpus')
    print len(c)
    
Exceptions
----------

.. autoclass:: corpora.Corpus
   

