

#str_n=input("请输入一个正整数：")
#int_n=int(str_n)

n=int(input("请输入一个正整数："))
print("我的n=",n)
x=0
for i in range(1,n+1):
    for j in range(1,i+1):
        x=x+j
print("s=",x)