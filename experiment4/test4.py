kg=input("请输入您的体重(kg）：")
kg=float(kg)

cm=input("请输入您的身高(cm）：")
cm=float(cm)
cm=cm/100#转换成以米为单位的长度

BMI=kg/(cm**2)
#print(BMI)

if BMI <18.5:
    print("过轻",BMI)
elif BMI>=18.5 and BMI<25:
    print("正常",BMI)
elif BMI>=25 and BMI<28:
    print("过重",BMI)
elif BMI >= 28 and BMI < 32:
    print("肥胖",BMI)
else:
    print("严重肥胖",BMI)
print("baihujunjun")