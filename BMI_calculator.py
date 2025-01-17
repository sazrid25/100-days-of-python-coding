# Body Mass Index Calculator in metric  units

weight = float(input("what is your weight in kg?\n"))
height = float(input("what is your height in m?\n"))

bmi = weight / height**2

print("your BMI is " + str(round(bmi, 6)))



# BMI range for Men

# Under 18.5      : Underweight
# 18.5–24.9       : Healthy weight
# 25.0–29.9       : Overweight
# 30.0 or greater : Obese
# 40 or above     : Severely obese