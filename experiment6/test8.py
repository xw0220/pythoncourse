def qiuhe(x):
    feizhengshuliebiao=[]
    if x==[]:
        return "输入不能为空列表"
    else:
        for item in x:
            if type(item)!=int:
                feizhengshuliebiao.append((item,type(item)))
        if feizhengshuliebiao==[]:
            return sum(x)
        else:
            print("元素类型错误，要求所有元素都为整数")
            return feizhengshuliebiao
m=[1,2,3,4,5]
n=[1,'bai','hu',3,4]
print(qiuhe(n))