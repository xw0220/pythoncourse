'''
fruit=["apple","banana","orange"]

for x in fruit:
    print(x)

#print(len(fruit))
i=1
while i<=len(fruit):
    print(fruit[i-1])
    i=i+1
'''
'''
print("1")
print("2")
print("3")
#如果是语法错误，程序肯定崩溃，并定位到下面连接的第一行语句
#如果最后缺少括号，则报错说缺少预期符号。
#如果是逻辑错误，则使用try语句进行错误提示。

y=list(range(1,21))
print(y)
for x in y:
    print("{}/2的类型是{}".format(x,type(x/2)))
    print(type(x))
    print(x/2)
    if type(x/2)==int:
        print(x)
'''
'''
print(list(range(5)))
print(int('ssd'))
'''

for x in range(1,11):
    if x%2==0:
        print(x)

for x in range(2,11,3):
    print(x)