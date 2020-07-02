# read https://forum.qt.io/topic/80928/problem-building-oci-plugin-for-qt-5-9-1/11
d:
cd D:\Work\qt5\qtbase\src\plugins\sqldrivers\oci
set INCLUDE=%INCLUDE%;D:\FOROCI\oci\include
set LIB=%LIB%;D:\FOROCI\oci\lib\msvc
D:\Work\qt5\qtbase\bin\qmake "INCLUDEPATH+=D:/FOROCI/oci/include" "LIBS+=-LD:/FOROCI/oci/lib/msvc -loci" oci.pro
nmake
