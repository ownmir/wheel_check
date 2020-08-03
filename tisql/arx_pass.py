import sys
import subprocess
import hashlib

sys.path.append(r"C:\Program Files\7-zip")
sys.path.append(r"D:\TMP")
#save
filename = 'mani.py'
filesalt = ''
with open(filename, 'rb') as f:
    m = hashlib.md5()
    while True:
       data = f.read(8192)
       if not data:
           break
       m.update(data)
    myhash = m.hexdigest()
# myhash = 'e5f6'
print(myhash)
#za = subprocess.call(['zip', '-e', '-P', myhash, 'avv', 'avv'])
za = subprocess.call(['7z', 'a', '-P'+myhash, 'avv', filename])
print(za)
# test
with open("hdatabase", "r", encoding='utf-8') as tst:
   lines = f.readlines()
   try:
       self.interval_e.setText(lines[0])
   except:
       self.error_label.setText(' Возможно в первой строке файла hdatabase нет line!')
input("Modification of " + filename + " file is blocked")

