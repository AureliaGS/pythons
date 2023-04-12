# BMI
# body mass index calculator
# BMI = weight(kg)/height(m)^2
# <15 = very severely underweight
# 15 to 16 = severely underweight
# 16 to 18.5 = underweight
# 18.5 to 25 = normal
# 25 to 30 = overweight
# 30 to 35 = moderately obese
# 35 to 40 = severely obese
# >40 = very severely obese

def report(BMI):
    if BMI < 15:
        result='very severely underweight'
    elif (BMI >= 15) and (BMI < 16):
        result='severely underweight'
    elif (BMI >= 16) and (BMI < 18.5):
        result='underweight'
    elif (BMI >= 18.5) and (BMI < 25):
        result='normal'
    elif (BMI >= 25) and (BMI < 30):
        result='overweight'
    elif (BMI >= 30) and (BMI < 35):
        result='moderately obese'
    elif (BMI >= 35) and (BMI < 40):
        result='severely obese'
    else:
        result='very severely obese'
    return result


while True: 
    weight = float(input('How much do you weigh in kg?'))
    height = float(input('Enter your height in meters?'))
    BMI = round(weight/(height*height),2)
    print('Your BMI is ' + str(BMI))
    print('You are:')
    
    augusta = report(BMI)
    print(augusta)

    answer = input('More? (y/n) ')
    if answer == "n":
        break
