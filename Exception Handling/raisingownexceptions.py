from math import pow

height = float(input("Height in metres:"))
weight = int(input("Weight in kgs:"))

if height > 3:
    raise ValueError("Human height should not exceed 3 metres!!")

bmi = weight / pow(height, 2)
print(f"BMI is {bmi}")