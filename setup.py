from distutils.core import setup, Extension

setup(name = "pyspamsum",
    version = "1.0.1",
    author = "Russell Keith-Magee",
    author_email = "russell@keith-magee.com",
    url = 'http://code.google.com/p/pyspamsum/',
    license = "New BSD",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    platforms = ["any"],
    description = "A Python wrapper for Andrew Tridgell's spamsum algorithm",
    long_description = """
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
""",
    ext_modules = [
        Extension(
            "spamsum", [
                "pyspamsum.c",
                "spamsum.c",
                "edit_dist.c",
            ]
        )
    ]
)
