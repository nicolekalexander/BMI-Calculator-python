from colorama import Fore, Back, Style

def bmi_calculator(weight, height):
    bmi_constant = 703
    bmi_status = None

    BMI = (weight * bmi_constant) / (height**2) 
    
    if BMI < 18.5:
        bmi_status = "underweight"
    elif BMI < 25:
        bmi_status = "normal weight"
    elif BMI < 30:
        bmi_status = "overweight"
    else: 
        bmi_status = "obese"
    
    return (" \n The BMI for a height of " + str(height) + " inches and a weight of " + str(weight) + " pounds is " + str(BMI) + ". This person would be considered " + bmi_status + ". \n")

userWeight = int(raw_input(Fore.GREEN + "\n Enter your weight in pounds: " + Fore.WHITE))
userHeight = int(raw_input(Fore.GREEN + "\n Enter your height in inches: " + Fore.WHITE))

print(Fore.CYAN + bmi_calculator(userWeight, userHeight))
print(Style.RESET_ALL)