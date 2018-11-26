input_str=None
num_list=[]#创建一个空列表
while input_str != 'done':
    input_str=input("请输入一个整数：")
    if input_str !='done':
        num_list.append(int(input_str))#给列表赋值
print(num_list)
temp=None
num_len=len(num_list)
for i in range(0,num_len-1):
    for j in range(i+1,num_len):
        print("i={},j={}".format(num_list[i],num_list[j]))
        if num_list[i]>num_list[j]:
            temp=num_list[i]
            num_list[i]=num_list[j]
            num_list[j]=temp
print(num_list)

