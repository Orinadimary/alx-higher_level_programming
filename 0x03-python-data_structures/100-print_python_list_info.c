#include <Python.h>

/**
 * print_python - Create a C function that prints some basic info about Python lists
 * @p: pointer to the object
 */
void print_python_list_info(PyObject *p)
{       
        int len,y,z;
        PyObject *obj;

        len = Py_LEN(p);
        y = ((PyListObject *)p)->allocated;

        printf("[*] Size of the Python List = %d\n", len);
        printf("[*] Allocated = %d\n", y);

        for (z = 0; z < len; z++)
        {
                printf("Element %d: ", z);

                obj = PyList_GetItem(p, z);
                printf("%s\n", Py_TYPE(obj)->tp_name);
        }
}
