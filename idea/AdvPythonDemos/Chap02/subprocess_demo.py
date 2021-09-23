import subprocess

m = subprocess.run("dir", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
print(m)
