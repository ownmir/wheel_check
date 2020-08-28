#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
//#include <conio.h>
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
    printf("Py_Initialized\n");
    const char* script_path = "tk1.py";
    //https://stackoverflow.com/questions/3654652/why-does-the-python-c-api-crash-on-pyrun-simplefile
    //PyObject *obj = Py_BuildValue("s", script_path);
    FILE *file = _Py_fopen(script_path, "r+");
    char* py_argv[] = {strdup(script_path)};
    PySys_SetArgv(1, py_argv);
    if(file != NULL) {
      PyRun_SimpleFile(file, script_path);
    }
    /*PyRun_SimpleString("from time import time,ctime\n"
                       "print('Today is', ctime(time()))\n");
    char* py_argv[] = {strdup(script_path), strdup("argument")};
    PySys_SetArgv(2, py_argv);*/
    //FILE *fp = fopen(script_path, "r+");
    //if (fp == NULL) {printf("Dont open file");}
    printf("script_path %s\n", script_path);
    //int res = PyRun_SimpleFileEx(fp, script_path, 1);
    //printf("res?\n");
    //printf("res%d", res);
    // free(py_argv[0]);
    if (Py_FinalizeEx() < 0) {
        printf("exit(120)");
        exit(120);
    }
    PyMem_RawFree(program);
    printf("exit(0)");
    return 0;
}
