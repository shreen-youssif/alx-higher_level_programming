#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @py_list: A PyObject list.
 */
void print_python_list_info(PyObject *py_list)
{
    int list_size, list_allocated, index;
    PyObject *list_item;

    list_size = Py_SIZE(py_list);
    list_allocated = ((PyListObject *)py_list)->allocated;

    printf("[*] Size of the Python List = %d\n", list_size);
    printf("[*] Allocated = %d\n", list_allocated);

    for (index = 0; index < list_size; index++)
    {
        printf("Element %d: ", index);

        list_item = PyList_GetItem(py_list, index);
        printf("%s\n", Py_TYPE(list_item)->tp_name);
    }
}
