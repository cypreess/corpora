Corpus internal format
======================
Single corpus is stored as a directory. In the directory there are several files important for corpus structure.


File ``config``
---------------
This file stores yaml formatted dict with properties of corpus. A typical ``config`` file has following properties:
::
    
    chunk_size: 52428800
    current_chunk: 0
    encoding: utf-8
    name: 50k Internet Corpus
    

.. warning::

    you should not modify ``config`` file by yourself, unless you really know what you do.


``chunk_size``
    max size (in bytes) of single corpus chunk 

.. note::

    single document must be stored within single chunk, so you cannot store documents larger that ``chunk_size``.


``current_chunk``
    number of current chunk that will be used when appending new document; 

.. note::

    chunks are numbered from 0.

``encoding``
    internal chunk encoding; possibly always ``utf-8``.

``name``
    an optional name for corpus


File ``chunkN``
---------------
Files like ``chunk0``, ``chunk1``, ``chunk2``, ... contains raw texts and headers. Each chunk can have maximum size of ``chunk_size`` bytes config property.

Chunk file has a very simple internal format. Documents are stored sequentially (one after another). Each document is represented as yamled header dict and raw document text encoded with ``encoding`` defined in ``config`` file.

Internal format of chunk is:
::
    
    [yamled header1]\n
    [raw document1 text encoded]\n
    [yamled header2]\n
    [raw document2 text encoded]\n
    ...
    [yamled headern]\n
    [raw documentn text encoded]\n

.. note::

    chunks are numbered from 0.

.. note::

    single document must be stored within single chunk, so you cannot store documents larger that ``chunk_size``.
    
An example of two documents long chunk:
::
    
    id: 8
    Prof. Wojciech Roszkowski jest oficjalnym kandydatem AWS na 
    prezesa Instytutu Pamięci Narodowej - zdecydowało prezydium 
    Klubu Parlamentarnego Akcji Wyborczej Solidarność.
    Rzecznik klubu Piotr Żak przypomniał, że zgodnie z ustawą o IPN, 
    Sejm wybiera prezesa Instytutu większością 3/5. Do wyboru 
    Roszkowskiego konieczne jest zatem uzyskanie poparcia nie tylko 
    Unii Wolności, ale także Polskiego Stronnictwa Ludowego.
    Politycy PSL, UW i SLD odmawiają deklaracji, czy ich ugrupowania 
    poprą kandydaturę prof. Roszkowskiego.
    
    id: 20
    Papieże Pius IX i Jan XXIII zostaną beatyfikowani 3 września - 
    ogłosił Watykan. Beatyfikacja obu papieży zbiegnie się z 
    uroczystościami Wielkiego Jubileuszu Roku 2000. 

File ``idx``
------------
This file contains a list of documents descriptors (indexes in chunk file). This is serialized  list, that contains a tuples like:
    * chunk number
    * offset of document start in chunk file
    * length of header section (with additional ``\n`` )
    * length of text section (with additional ``\n``)

Currently the serialization is made with cPickle.

File ``ridx``
-------------
This files stores a random access index. Basically it is a dict containing a mapping of document ``id`` to the index in ``idx`` list. 

Currently this is cPickle serialized dict.



