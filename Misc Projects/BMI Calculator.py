print ("BMI Calculator")
Height = float(input("What's your Height (in meters): "))
Weight = float(input("What's your Weight (in Kg): "))
bmi = Weight / Height**2
BMI = round(bmi , 2)

if bmi >= 25:
    print(f"You are Overweight & Need to Reduce Weight: BMI {BMI}")
elif bmi >= 18.5:
    print(f"Your Weight is Normal: BMI {BMI}")
else:
    print(f"You are Underweight: BMI {BMI}")