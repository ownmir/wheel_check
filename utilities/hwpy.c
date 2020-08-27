#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <conio.h>
//#include <cstring>
//#include <cstdio>

int
main(int argc, char *argv[])
{
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }
    Py_SetProgramName(program);  /* optional but recommended */
    Py_Initialize();
    prinf("Py_Initialized");
    const char* script_path = "script.py";
    /*PyRun_SimpleString("from time import time,ctime\n"
                       "print('Today is', ctime(time()))\n");
    char* py_argv[] = {strdup(script_path), strdup("argument")};
    PySys_SetArgv(2, py_argv);*/
    int res = PyRun_SimpleFileEx(fopen(script_path, "rb"), script_path, 1);
    printf("res%d", res);
    // free(py_argv[0]);
    if (Py_FinalizeEx() < 0) {
        exit(120);
    }
    PyMem_RawFree(program);
    return 0;
}
