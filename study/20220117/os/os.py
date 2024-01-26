import os
# print(os.environ)

# print(os.environ['PATH'])

# print(os.chdir("C:\WINDOWS"))

# print(os.getcwd())

# print(os.system("dir"))

f = os.popen("dir")
print(f)
print(f.read())