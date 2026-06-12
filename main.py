from Function import *

operation=input("please enter the operation you want : multiply , add , minus , divide , cos , sin , tan : ")
x=input("please enter the numbers : ").split()
if operation=="add":
    print(add(*map(int,x)))
elif operation=="minus":
    print(minus(*map(int,x)))
elif operation=="multiply":
    print(multiply(*map(int,x)))
elif operation=="divide":
    print(divide(*map(int,x)))
elif operation=="cos":    
    cosFun(*map(int,x))
elif operation=="sin":    
    sinFun(*map(int,x))