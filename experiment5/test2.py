'''
try:
    print("right")
except:
    print("wrong")
else:
    print("you are right")

print("others")
'''


'''
i=0
while i<=(len(fruit)-1):
    print(fruit[i])
    i=i+1
'''

#print(list(range(1,10)))
'''
n=int(input("请输入一个数："))
num=list(range(1,n+1))
for i in num:
    #print(num[i-1])
    if num[i-1]%2==1:
        print(num[i-1])
'''

for i in range(1,10):
    for j in range(1,i+1):
        print("{0}x{1}={2} ".format(i,j,i*j),end='')
        #print(i,j)
    print("\n")

