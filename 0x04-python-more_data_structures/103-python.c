#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int s;
	int j;
	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &trying_str, &s);

	printf("  size: %li\n", s);
	printf("  trying string: %s\n", trying_str);
	if (s < 10)
		printf("  first %li bytes:", s + 1);
	else
		printf("  first 10 bytes:");
	for (j = 0; j <= s && j < 10; j++)
		printf(" %02hhx", trying_str[j]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int s = PyList_Size(p);
        int j;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", s);
        printf("[*] Allocated = %li\n", list->allocated);
        for (j = 0; j < s; j++)
        {
                type = (list->ob_item[j])->ob_type->tp_name;
		printf("Element %i: %s\n", j, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[j]);
        }
}
