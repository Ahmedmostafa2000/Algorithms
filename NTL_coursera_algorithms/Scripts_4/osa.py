import os
os.system("ipconfig")
f = os.popen('dir')
now = f.read()
print (now)