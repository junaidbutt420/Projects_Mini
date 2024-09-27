nam = input("Enter The Name ?")
try: 
   weight = int(input("Enter your Weight in pounds "))
   height = int(input("Enter your height in inchies "))
except ValueError:
    print("Invalid Input")
else:
    BMI = (weight * 703) / (height * height )
    print(BMI)
    if BMI>0:
        if BMI<18.5:
            print(nam,', you are Underweight')
        elif BMI<=24.9:
            print(nam,', you are Normal Weight!')
        elif BMI<=29.9:
            print(nam,', you are Overweight')
        elif BMI<=34.9:
            print(nam,', you are Obese')
        elif (BMI<=39.9):
            print(nam,", you are severely obese.")
        else:
            print(nam,", you are morbidly obese.")
    else:
        print("Enter valid input")
