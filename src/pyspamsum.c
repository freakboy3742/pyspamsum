/**
 * PySpamsum v1.0.0
 *
 * A Python wrapper around the spamsum library written by
 * Andrew Tridgell.
 *
 * Copyright 2009 Russell Keith-Magee <russell@keith-magee.com>
 */

#define PY_SSIZE_T_CLEAN

#include <Python.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>

int edit_distn(char *from, int from_len, char *to, int to_len);
char *spamsum(const unsigned char *in, unsigned int length, unsigned int flags, unsigned int bsize);
unsigned int spamsum_match(const char *str1, const char *str2);

struct module_state {
    PyObject *error;
};

#define GETSTATE(m) ((struct module_state*)PyModule_GetState(m))

PyObject *py_edit_distance(PyObject *self, PyObject *args)
{
    PyObject *result = NULL;
    int distance;

    char *from, *to;
    Py_ssize_t from_len, to_len;

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
    Py_ssize_t length;
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

static int spamsum_traverse(PyObject *m, visitproc visit, void *arg) {
    Py_VISIT(GETSTATE(m)->error);
    return 0;
}

static int spamsum_clear(PyObject *m) {
    Py_CLEAR(GETSTATE(m)->error);
    return 0;
}
static struct PyModuleDef ss =
{
    PyModuleDef_HEAD_INIT,
    "spamsum",
    "",
    sizeof(struct module_state),
    methods,
    NULL,
    spamsum_traverse,
    spamsum_clear,
    NULL
};

PyMODINIT_FUNC
PyInit_spamsum(void)
{
    PyObject *module = PyModule_Create(&ss);

    if (module == NULL) {
        return NULL;
    }
#ifdef Py_GIL_DISABLED
    PyUnstable_Module_SetGIL(module, Py_MOD_GIL_NOT_USED);
#endif

    struct module_state *st = GETSTATE(module);

    st->error = PyErr_NewException("spamsum.Error", NULL, NULL);
    if (st->error == NULL) {
        Py_DECREF(module);
        return NULL;
    }

    return module;
}
