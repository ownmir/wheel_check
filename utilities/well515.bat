# read https://forum.qt.io/topic/80928/problem-building-oci-plugin-for-qt-5-9-1/11
# download https://download.qt.io/official_releases/qt/5.15/5.15.0/submodules/
d:
cd D:\Work\qt5.15.0\qtbase-everywhere-src-5.15.0\src\plugins\sqldrivers
D:\Work\qt5.15.0\qtbase-everywhere-src-5.15.0\bin\qmake sqldrivers.pro
cd D:\Work\qt5.15.0\qtbase-everywhere-src-5.15.0\src\plugins\sqldrivers\oci
set INCLUDE=%INCLUDE%;D:\FOROCI\oci\include
set LIB=%LIB%;D:\FOROCI\oci\lib\msvc
D:\Work\qt5.15.0\qtbase-everywhere-src-5.15.0\bin\qmake "INCLUDEPATH+=D:/FOROCI/oci/include" "LIBS+=-LD:/FOROCI/oci/lib/msvc -loci" oci.pro
#nmake
