#languages: calling C from Python
#Developed on the stud.cs.smu.ca linux server
from ctypes import *
direct = input("CFile.so path as string = ")
so_file = direct
my_functions = CDLL(so_file)

a = input("input a ")
b = input("input b ")
c = input("input c ")
print(my_functions.myFunc(a, b, c))
