# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / height ** 2

f_bmi = float("{:.2f}".format(bmi))

if f_bmi <= 35:
    if f_bmi <= 18.5:
        simple_bmi = int(round(f_bmi, 0))
        print(f"Your BMI is {simple_bmi}, you are under weight.")
    elif f_bmi >= 18.6 and f_bmi <= 25 :
        simple_bmi = int(round(f_bmi, 0))
        print(f"Your BMI is {simple_bmi}, you have a normal weight.")
    elif f_bmi > 25 and bmi < 30:
        simple_bmi = int(round(f_bmi, 0))
        print(f"Your BMI is {simple_bmi}, you are slightly overweight.")
    else:
        simple_bmi = int(round(f_bmi, 0))
        print(f"Your BMI is {simple_bmi}, you are obese.")
else:
    simple_bmi = int(round(f_bmi, 0))
    print(f"Your BMI is {simple_bmi}, you are clinically obese.")
