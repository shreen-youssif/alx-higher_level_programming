#include <Python.h>

/**
 * print_python_bytes - Print basic info about Python bytes objects
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
	char *str = NULL;
	Py_ssize_t size = 0, i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size > 10)
		size = 10;

	printf("  first %ld bytes:", size);

	for (i = 0; i < size; i++)
		printf(" %02x", str[i] & 0xFF);

	printf("\n");
}

/**
 * print_python_list - Print basic info about Python lists
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *element;

	printf("[*] Python list info\n");

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);

		if (PyBytes_Check(element))
			print_python_bytes(element);
	}
}
