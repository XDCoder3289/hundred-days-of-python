# A BMI calculator

height = float(input("Please enter your height: "))
weight = float(input("Please enter your weight: "))

bmi = weight / (height ** 2)

print("Your BMI is: " + str(bmi))

