import os
import stat
import pickle
import shutil
from Cryptodome.Cipher import DES
import zipfile
import sys

def pad(text):

    while len(text) % 8 != 0:
        text += b' '
    return text


class Error(OSError):
    pass


def copyfileobj(fsrc, fdst, length=16*1024):
    """copy data from file-like object fsrc to file-like object fdst"""
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break
        if to_en:
            fdst.write(des.encrypt(pad(buf)))
        else:
            fdst.write(des.decrypt(buf))


def copyfile(src, dst, *, follow_symlinks=True):
    """Copy data from src to dst.

    If follow_symlinks is not set and src is a symbolic link, a new
    symlink will be created instead of copying the file it points to.

    """
    # if _samefile(src, dst):
    #     raise SameFileError("{!r} and {!r} are the same file".format(src, dst))

    for fn in [src, dst]:
        try:
            st = os.stat(fn)
        except OSError:
            # File most likely does not exist
            pass
        else:
            # XXX What about other special files? (sockets, devices...)
            if stat.S_ISFIFO(st.st_mode):
                raise SpecialFileError("`%s` is a named pipe" % fn)

    if not follow_symlinks and os.path.islink(src):
        os.symlink(os.readlink(src), dst)
    else:
        with open(src, 'rb') as fsrc:
            with open(dst, 'wb') as fdst:
                copyfileobj(fsrc, fdst)
    return dst


def copy2(src, dst, *, follow_symlinks=True):
    """Copy data and metadata. Return the file's destination.

    Metadata is copied with copystat(). Please see the copystat function
    for more information.

    The destination may be a directory.

    If follow_symlinks is false, symlinks won't be followed. This
    resembles GNU's "cp -P src dst".

    """
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    copyfile(src, dst, follow_symlinks=follow_symlinks)
    #copystat(src, dst, follow_symlinks=follow_symlinks)
    return dst


def to(src, dst, symlinks=False, ignore=None, copy_function=copy2,
             ignore_dangling_symlinks=False):
    #d = shutil.copytree('itest', 'to', ignore=shutil.ignore_patterns('__pycache__'))
    #return
    names = os.listdir(src)
    # print('names', names)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()
    os.makedirs(dst)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        #print('srcname', srcname, 'type(srcname)', type(srcname))
        dstname = os.path.join(dst, name)
        #print('dstname', dstname)
        try:
            if os.path.islink(srcname):
                linkto = os.readlink(srcname)
                if symlinks:
                    # We can't just leave it to `copy_function` because legacy
                    # code with a custom `copy_function` may rely on copytree
                    # doing the right thing.
                    os.symlink(linkto, dstname)
                    # shutil.copystat(srcname, dstname, follow_symlinks=not symlinks)
                else:
                    # ignore dangling symlink if the flag is on
                    if not os.path.exists(linkto) and ignore_dangling_symlinks:
                        continue
                    # otherwise let the copy occurs. copy2 will raise an error
                    if os.path.isdir(srcname):

                        # copytree(srcname, dstname, symlinks, ignore,
                        #          copy_function)
                        to(srcname, dstname, symlinks, ignore,
                                 copy_function)
                    else:
                        # print('srcname', srcname, 'type(srcname)', type(srcname))
                        copy_function(srcname, dstname)
            elif os.path.isdir(srcname):
                # copytree(srcname, dstname, symlinks, ignore, copy_function)
                to(srcname, dstname, symlinks, ignore, copy_function)
            else:
                # Will raise a SpecialFileError for unsupported file types
                # print('Will raise a SpecialFileError for unsupported file types', dstname)
                copy_function(srcname, dstname)
                # catch the Error from the recursive copytree so that we can
            # continue with other files
        except Error as err:
            errors.extend(err.args[0])
        except OSError as why:
            errors.append((srcname, dstname, str(why)))
        # try:
        #     shutil.copystat(src, dst)
        # except OSError as why:
        #     # Copying file access times may fail on Windows
        #     if getattr(why, 'winerror', None) is None:
        #         errors.append((src, dst, str(why)))
        if errors:
            raise Error(errors)
    return


to_en = False
with open('gold', 'rb') as gold:
    key = gold.read(int(sys.argv[1]))
des = DES.new(key, DES.MODE_ECB)
if __name__ == '__main__':
    to_en = True
    to(sys.argv[2], 'to', ignore=shutil.ignore_patterns('__pycache__', '.*'))
    to_zip = zipfile.ZipFile('to.zip', 'w')
    for folder, subfolders, files in os.walk('to'):
        for file in files:
            to_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'to'),
                         compress_type=zipfile.ZIP_DEFLATED)
    to_zip.close()
    to_en = False
    #to('to', 'from', ignore=shutil.ignore_patterns('__pycache__', '.*'))
