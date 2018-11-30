#函数定义的范例
def fib(n):
    '''输入一个正整数n，返回一列斐波那契数列，数列的最后一个元素小于n'''#这一段可以用来对函数进行说明
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()
fib(1000)

def printMax(a,b):
    if a>b:
        print(a, ' is the max')
    else:
        print(b, ' is the max')
printMax(4,5)

def addOne(a):
    print(a)
    a +=1
    print(a)
a=3
addOne(a)
print(a)

def modify(v):
    v[0]=v[0]+1
a=[2]
modify(a)
print(a)

def modify_add(v,item):
    v.append(item)
a=[2]
modify_add(a,3)
print(a)

def modify_dic(d):
    d['age']=38
a={'name':'Dong','age':37,'sex':'Male'}
print(a)
modify_dic(a)
print(a)

def demo_1(*p):
    print(p)
demo_1(1,2,3,8,9)

def demo_2(**p):
    for item in p.items():
        print(item)
demo_2(x=1,y=2,z=3)

def demon_3(a,b,c):
    print(a+b+c)
seq=[1,2,3]
demon_3(*seq)

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

