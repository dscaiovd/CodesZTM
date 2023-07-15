#defining the BMI by male or female
def funcmale(bmi):
    if bmi < 26.4 and bmi > 20.7:
        print(str("You are on the perfect weight!"))
    elif bmi < 20.7:
        print(str("You are too low on the perfect weight."))
    elif bmi > 26.4:
        print(str("You are too heaavy for the perfect weight."))

def funcfemale(bmi):
    if bmi < 24.9 and bmi > 18.5:
        print(str("You are on the perfect weight!"))
    elif bmi < 18.5:
        print(str("You are too low on the perfect weight."))
    elif bmi > 24.9:
        print(str("You are too heaavy for the perfect weight."))

#variables
height = float(input("Insert your height: "))
weight = float(input("Insert your weight: "))

#defining the calculation of the body mass index
bmi = weight / (height ** 2)

while True:
    sex = str(input("Please insert your biological gender: ").lower())
    if sex == "male":
        funcmale(bmi)
        break
    elif sex == "female":
        funcfemale(bmi)
        break
    else:
        print("Invalid gender, try again.")