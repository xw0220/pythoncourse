n=input("please input an integer:")
n=int(n)
factor=1
i=1

while i<=n:
    print('{}*{}={}'.format(factor,i,factor*i))
    factor=factor*i
    i=i+1

print("the factor is:",factor)
print("baihu")
