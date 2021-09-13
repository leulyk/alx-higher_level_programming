#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - print some basic info about python lists
 *
 * @p: the PyObject to analyse
 *
 */
void print_python_list_info(PyObject *p)
{
	long int size, nalloc, i;
	PyObject *item;

	size = (PyList_Size)(p);
	nalloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", nalloc);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
