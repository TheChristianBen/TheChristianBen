from math import sqrt
import textwrap

while True:
    try:
        num = float(input("Enter your number: "))
        if num >= 1:
            break
        else:
            print("Error! Please enter a positive number.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        
if num >= 1:
    rootfloat = sqrt(num)
    rootint = int(sqrt(num))
    print(f"The Float Value is: {rootfloat:.2f}")
    print(f"The Integer Value is: {rootint}")
else:
    print("Error!\nPlease Enter A Postive Number")

question = input("Do you wanna know why Integer value is less(Yes/No)?? ").strip().lower()

Yes = ("yes", "s", "yeah", "yea", "ye", "y")
No = ("no", "nah", "na", "n")

if question in Yes:
    explanation = "The Integer value is calculated by using explicit type conversion method that forces the float value to convert into integer value by removing the data after the decimal point, eventually losing a huge amount of data"
    print("\n" + textwrap.fill(explanation))
elif question in No:
    print("Alright Thank You!!")
else:
    print("Invalid response! Please enter Yes or No.")
