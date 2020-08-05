import sys
import subprocess
import hashlib
from getpass import getpass

def mixing_lists(*args):
   result = ''
   for arg in zip(args):
      for item in arg:
         result += item
   return result
   
sys.path.append(r"C:\Program Files\7-zip")
print(sys.path)
#save
filename = 'mani.py'
filesalt = 'salt'
with open("D:/TMP/salt", "r", encoding='utf-8') as slt:
   lines = slt.readlines()
   try:
       salt = lines[0]
   except:
       self.error_label.setText(' Возможно в первой строке файла соли нет line!')
#
passw = getpass('Please enter your password ')
hard = mixing_lists(passw, salt)
print(hard)
with open(filename, 'rb') as f:
    m = hashlib.md5()
    while True:
       data = f.read(8192)
       if not data:
           break
       m.update(data)
    myhash = m.hexdigest()
    m.update(hard.encode('utf-8'))
    hard_myhash = m.hexdigest()
# myhash = 'e5f6'
print('simply', myhash)
print('hard', hard_myhash)
with open("hdatabase", "w", encoding='utf-8') as hsh:
   hsh.write(hard_myhash)
#za = subprocess.call(['zip', '-e', '-P', myhash, 'avv', 'avv'])
za = subprocess.check_output(['7z', 'a', '-P'+myhash, 'avv', filename], shell=True)
# za = subprocess.call(['7z.exe'], shell=True)
print(za)
# test
with open("hdatabase", "r", encoding='utf-8') as hsh:
   lines = hsh.readlines()
   try:
       print(lines[0])
   except:
       self.error_label.setText(' Возможно в первой строке файла hdatabase нет line!')
input("Modification of " + filename + " file is blocked")

