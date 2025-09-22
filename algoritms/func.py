import math
from math import log2,floor
def funс(n:int):
    if n==0:return 1
    counter = 0
    tmp = n
    while tmp!=0:
        tmp//=2
        counter+=1
    # print(2**counter)
    return counter
print(funс(2))

def funс(n:int):
    if n == 0: return 1
    return floor((log2(n)))+1
print(funс(4))

def funс(n:int):
    return  n.bit_length()
print(funс(2))

def funс(n:int):
    if n==0:return 0
    if n==1:return 1
    return 1+funс(n//2)

print(funс(3))
