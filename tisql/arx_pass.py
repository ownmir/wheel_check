import subprocess

myhash = 'e5f6'
za = subprocess.call(['zip', '-e', '-P', myhash, 'avv', 'avv'])
print(za)
