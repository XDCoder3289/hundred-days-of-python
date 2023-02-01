height = float(input("Please enter your height: "))
weight = float(input("Please enter your weight: "))

bmi = round(weight / height ** 2)

if bmi < float(18.5):
    print(f"You're underweight, bmi: {bmi}")
elif bmi < float(25):
    print(f"You have a normal weight, bmi: {bmi}")
elif bmi < float(30):
    print(f"You are overweight, BMI: {bmi}")
elif bmi < float(35):
    print(f"You are obese: BMI: {bmi}")
elif bmi > float(35):
    print(f"Lose some fucking weight you whale, BMI: {bmi}")
else:
    print("Sorry")