'''
age=11
if age==10:
    print("你今年10岁了")
elif age==11:
    print("你今年11岁了")
elif age==12:
    print("你今年12岁了")
else:
    print("哎呀，我已经算不过来了")
'''
'''
age=None
if age==None:
    print("what is 13+49+29383+83838? headache!")
else:
    print("so easy")
'''
'''
a=10
b='10'
if a==b:
    print("same")
else:
    print("different")

content=input("please input a number:")
print(type(int(content)))
if int(content) >100:
    print("您真长寿")
'''
'''
n=1
x=1
while n<=9:
    print('{}*{}={}'.format(x,n+1,x * (n + 1)))
    x = x * (n + 1)
    n=n+1
print("x=",x)
'''
a=input("请输入第一个数：")#从键盘获得一个输入
a=int(a)#把输入的字符串转换成数字类型
print(a)
print(type(a))











