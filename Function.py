from math import *

def add(*x):
    total=0
    for i in x:
        total+=i
    return total

def minus(*x):
    total=x[0]
    for i in x[1::]:
        total-=i
    return total

def multiply(*x):
    total=x[0]
    for i in x[1::]:
        total*=i
    return total

def divide(*x):
    total=x[0]
    for i in x[1::]:
        total/=i
    return total

def cosFun(*x):
    for i in x :
        print(cos(i))


def sinFun(*x):
    for i in x :
        print(sin(i))

def tanFun(*x):
    for i in x :
        print(tan(i))


