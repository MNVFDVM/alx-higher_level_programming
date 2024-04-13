#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int l;
	wchar_t *wide_str;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("	[ERROR] Invalid String Object\n");
		return;
	}

	l = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("	type: compact ascii\n");
	else
		printf("	type: compact unicode object\n");

	wide_str = PyUnicode_AsWideCharString(p, &l);
	if (wide_str == NULL) {
		printf("Failed to convert to wide character string\n");
		return;
	}

	printf("	length: %ld\n", l);
	wprintf(L"	value: %ls\n", wide_str);

	PyMem_Free(wide_str);
}
