def BMI(height,weight):
    '''
    height:cm
    weight:kg
    '''
    bmi_value=weight/((height/100)**2)
    bmi_status=None
    if bmi_value < 18.5:
        bmi_status="过轻"
    elif bmi_value >= 18.5 and bmi_value < 25:
        bmi_status = "正常"
    elif bmi_value >= 25 and bmi_value < 28:
        bmi_status = "过重"
    elif bmi_value >= 28 and bmi_value < 32:
        bmi_status = "肥胖"
    else:
        bmi_status = "严重肥胖"
    return((bmi_value,bmi_status))


print(BMI(155,52))
print(BMI(weight=52,height=155))