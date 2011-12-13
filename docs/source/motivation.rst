Motivation for corpora system
=============================
A natural language processing tasks involve using documents collections (for example `document retrieval`_ tasks). There are some ready python tools like NLTK_ but I found them too complicated for the simple purpose of storing a collection of raw text documents (for example gathered by a crawler). I have also needed a flexible way to store some meta information for each document, for example time of crawling, a semantic evaluation, md5 checksum or any other. It was also important to me to deal with a very large corpora, so system should avoid creating to big one flat file.

My typical use of corpora is append & read-only. For example I crawl a subset of webpages, and create a corpus of founded texts. Then I run some semantic evaluation on the corpus and creating next corpus of result set (or just store information about which documents id where matched). In this way I am avoiding a complex problem of dealing with updates, so system architecture can be very simple (new documents are just appended to the end of available chunk file).


.. _NLTK: http://www.nltk.org/
.. _`document retrieval`: http://en.wikipedia.org/wiki/Document_retrieval