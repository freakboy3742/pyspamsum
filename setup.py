#!/usr/bin/env python
import io

from setuptools import setup, Extension


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name="pyspamsum",
    version="1.0.5",
    description="A Python wrapper for Andrew Tridgell's spamsum algorithm",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author="Russell Keith-Magee",
    author_email="russell@keith-magee.com",
    url='http://github.com/freakboy3742/pyspamsum/',
    license="New BSD",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    ext_modules=[
        Extension(
            "spamsum", [
                "pyspamsum.c",
                "spamsum.c",
                "edit_dist.c",
            ]
        )
    ],
    test_suite='tests',
)
