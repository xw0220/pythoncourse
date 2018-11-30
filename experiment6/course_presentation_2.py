'''
from tkinter import *
root=Tk()
cv=Canvas(root, bg='white', width=300, height=320)
cv.create_line(10,10,100,160,width=8,dash=7)
cv.pack()
root.mainloop()

list=list(range(1,11))
for x in list:
    if x%2==0:
        print(x)
    else:
        print("奇数")
'''
f=lambda a,b,c:a+b+c
print(f(1,2,3))

f_1=lambda a,b:a*b
print(f_1(4,5))

def func_lib():
    def add(x, y):
        return x+y
    return add       # 返回函数对象
fadd = func_lib()
print(fadd(1, 2))

def fac(n):
   if n==1: #递归调用结束的条件
      p=1
   else:
      p=(fac(n-1)*n)  #调用fac( ) 函数本身
   return p
print(fac(4))

print(abs(-10))
print(2==2)
print(dir(2))
from math import sqrt
print(sqrt(4))