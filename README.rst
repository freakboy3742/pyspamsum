PySpamSum
=========

.. image:: https://img.shields.io/pypi/pyversions/pyspamsum.svg
    :target: https://pypi.org/project/pyspamsum

.. image:: https://img.shields.io/pypi/v/pyspamsum.svg
    :target: https://pypi.org/project/pyspamsum

.. image:: https://img.shields.io/pypi/status/pyspamsum.svg
    :target: https://pypi.org/project/pyspamsum

.. image:: https://img.shields.io/pypi/l/pyspamsum.svg
    :target: https://github.com/pybee/pyspamsum/blob/master/LICENSE

.. image:: https://travis-ci.org/pybee/pyspamsum.svg?branch=master
    :target: https://travis-ci.org/pybee/pyspamsum

spamsum is a fuzzy hash specifically designed for hashing email messages
to detect if they are SPAM. The spamsum utility includes the ability to
generate the spamsum hash and check a new message against a existing set
of hashes to find a match.

pyspamsum is a Python wrapper for the core API of spamsum.

The original spamsum code has been licensed under the terms of the
the Perl Artistic License. It has been slightly modified

The original code is Copyright Andrew Tridgell <tridge@samba.org> 2002.
It forms part of Andrew's junkcode, and is available here:

    http://www.samba.org/junkcode/#spamsum

The spamsum code in this project is derived from an updated version that
was published at Linux.conf.au 2004:

    http://linux.anu.edu.au/linux.conf.au/2004/papers/junkcode/spamsum

For details on spamsum itself, please see the spamsum README:

    http://samba.org/ftp/unpacked/junkcode/spamsum/README

Installation
------------

At a prompt, run::

    $ python setup.py install

Usage
-----

Once installed, here are some examples of usage::

    # Import spamsum and set up some strings
    >>> import spamsum
    >>> s1 = "I am the very model of a modern Major-General, I've information animal and vegetable and mineral"
    >>> s2 = "I am the very model of a modern Brigadier, I've information animal and vegetable and something else"
    >>> s3 = "Huh? Gilbert and Who?"

    # Evaluate the edit distance between two strings
    >>> spamsum.edit_distance(s1, s2)
    27

    # Evaluate the spamsum of some strings
    >>> sum1 = spamsum.spamsum(s1)
    >>> sum2 = spamsum.spamsum(s2)
    >>> sum3 = spamsum.spamsum(s2)
    >>> print sum1
    3:kEvyc/sFIKwYclQY4MKLFE4Igu0uLzIKygn:kE6Ai3KQ/MKOgDKZn

    # Compare two spamsums. 0 = no match, 100 = perfect match.
    >>> spamsum.match(sum1, sum1)
    100
    >>> spamsum.match(sum1, sum2)
    72
    >>> spamsum.match(sum1, sum3)
    0
