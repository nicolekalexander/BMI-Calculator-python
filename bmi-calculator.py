def bmi_calculator(age, weight, height):
    bmi_constant = 703
    BMI = (weight * bmi_constant) / (height**2) 
    return (BMI)

print(bmi_calculator(25, 139, 65))