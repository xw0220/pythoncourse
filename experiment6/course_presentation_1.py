
def order_my_list(num_list):
    temp=None
    num_len = len(num_list)
    for i in range(0, num_len - 1):
        for j in range(i + 1, num_len):
            print("i={},j={}".format(num_list[i], num_list[j]))
            if num_list[i] > num_list[j]:
                temp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = temp
    print(num_list)

my_list=[6,8,3,5]
#order_my_list(my_list)

def add_num(a,b):
    '''这是一个简单的加法器'''
    print(a+b)
#add_num(1,2)
#0,1,1,2,3,5,8,13,21

def fio(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()

#fio(100)
#fio(1000)
#fio(2000)

def hello_world(n=2):
    print("hello world."*n)
#hello_world(10)

def x(y):
    m=10*y
    return m
#print(x(8))

a_list=[9,3,4,6,5,8,7]
#min=sorted(a_list)[0]
#print(min)
#a_list.sort()[0]



w=10
def do_something():
    global w
    w=9
    print(w)
do_something()
print(w)
