import os
from Cryptodome.Cipher import DES
import zipfile
import shutil
from pack import to, to_en, des


if __name__ == '__main__':
    to_en = False
    to_zip = zipfile.ZipFile('to.zip')
    to_zip.extractall('from_zip')
    to_zip.close()
    to('from_zip', 'from', ignore=shutil.ignore_patterns('__pycache__', '.*'))
