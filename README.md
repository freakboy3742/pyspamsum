# PySpamSum

[![Python Versions](https://img.shields.io/pypi/pyversions/pyspamsum.svg)](https://pypi.python.org/pypi/pyspamsum)
[![PyPI Version](https://img.shields.io/pypi/v/pyspamsum.svg)](https://pypi.python.org/pypi/pyspamsum)
[![Maturity](https://img.shields.io/pypi/status/pyspamsum.svg)](https://pypi.python.org/pypi/pyspamsum)
[![BSD License](https://img.shields.io/pypi/l/pyspamsum.svg)](https://github.com/freakboy3742/pyspamsum/blob/main/LICENSE)
[![Build Status](https://github.com/freakboy3742/pyspamsum/workflows/CI/badge.svg?branch=main)](https://github.com/freakboy3742/pyspamsum/actions)

spamsum is a fuzzy hash specifically designed for hashing email messages
to detect if they are SPAM. The spamsum utility includes the ability to
generate the spamsum hash and check a new message against a existing set
of hashes to find a match.

pyspamsum is a Python wrapper for the core API of spamsum.

The original spamsum code has been licensed under the terms of the
the Perl Artistic License. It has been slightly modified to support
being packaged as a Python package, and to address some C code style
issues.

The original code is Copyright Andrew Tridgell
([tridge@samba.org](mailto:tridge@samba.org)) 2002. It forms part of Andrew's
junkcode, and is available:

* [on Github](https://github.com/tridge/junkcode/tree/master/spamsum)
* [On Andrew Tridgell's website](https://www.samba.org/ftp/unpacked/junkcode/spamsum/)

For details on spamsum itself, please see the README in the spamsum repo.

## Installation

At a prompt, run:

    $ python setup.py install

## Usage

Once installed, here are some examples of usage:

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
    >>> sum3 = spamsum.spamsum(s3)
    >>> print(sum1)
    3:kEvyc/sFIKwYclQY4MKLFE4Igu0uLzIKygn:kE6Ai3KQ/MKOgDKZn

    # Compare two spamsums. 0 = no match, 100 = perfect match.
    >>> spamsum.match(sum1, sum1)
    100
    >>> spamsum.match(sum1, sum2)
    72
    >>> spamsum.match(sum1, sum3)
    0
