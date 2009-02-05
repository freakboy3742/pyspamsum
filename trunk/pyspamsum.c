/**
 * PySpamsum v1.0.0
 *
 * A Python wrapper around the spamsum library written by
 * Andrew Tridgell.
 *
 * Copyright 2009 Russell Keith-Magee <russell@keith-magee.com>
 */
#include <Python.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>

int edit_distn(char *from, int from_len, char *to, int to_len);
char *spamsum(const unsigned char *in, size_t length, unsigned int flags, unsigned int bsize);
unsigned int spamsum_match(const char *str1, const char *str2);

PyObject *py_edit_distance(PyObject *self, PyObject *args)
{
    PyObject *result = NULL;
    int distance;

    char *from, *to;
    int from_len, to_len;

    if (!PyArg_ParseTuple(args, "s#s#", &from, &from_len, &to, &to_len))
    {
        return NULL;
    }

    distance = edit_distn(from, from_len, to, to_len);
    result = Py_BuildValue("i", distance);

    return result;
}


PyObject *py_spamsum(PyObject *self, PyObject *args)
{
    PyObject *result = NULL;
    char *sum;

    unsigned char *in;
    size_t length;
    unsigned int flags, bsize;

    flags = 0;
    bsize = 0;

    if (!PyArg_ParseTuple(args, "s#|ii", &in, &length, &flags, &bsize))
    {
        return NULL;
    }

    sum = spamsum(in, length, flags, bsize);
    result = Py_BuildValue("s", sum);
    free(sum);

    return result;
}

PyObject *py_match(PyObject *self, PyObject *args)
{
    PyObject *result = NULL;
    unsigned int match;
    char *str1, *str2;

    if (!PyArg_ParseTuple(args, "ss", &str1, &str2))
    {
        return NULL;
    }

    match = spamsum_match(str1, str2);
    result = Py_BuildValue("i", match);

    return result;
}


static PyMethodDef methods[] = {
    {"edit_distance", py_edit_distance, METH_VARARGS,
        "Calculate the edit distance between two strings."
    },
    {"spamsum", py_spamsum, METH_VARARGS,
        "Calculate the spamsum of a string."
    },
    {"match", py_match, METH_VARARGS,
        "Given two spamsum strings return a value indicating the degree to which they match."
    },
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initspamsum()
{
    (void) Py_InitModule("spamsum", methods);
}