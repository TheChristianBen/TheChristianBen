import math
def calculator():
    print("The Simple Calculator")
    print("Choose one of the below options by entering the corresponding number")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Exponents and Powers")
    print("5.Division")
    print("6.Hypotenuse")

    choice = input("Enter the option: ")

    try:
        if choice in ["1","2","3","4","5"]:
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))

            if choice == "1":
                print(f"Result: {num1 + num2}")
            elif choice == "2":
                print(f"Result: {num1 - num2}")
            elif choice == "3":
                print(f"Result: {num1 * num2}")
            elif choice == "4":
                if num1 < 0 and num2 != int(num2):
                    print("Can't raise a negative number to a decimal power.")
                else:
                    print(f"Result: {num1 ** num2}")
            elif choice == "5":
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Can't be divided by 0")
        elif choice == "6":
            side1 = float(input("Enter side A value: "))
            side2 = float(input("Enter side B value: "))
            hyp = math.sqrt(side1*side1 + side2*side2)
            print(f"Length of The Hypotenuse is: {hyp:.2f}")
        else:
            print("Invalid Option")

    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("0 can't be raised to a negative power.")
    except OverflowError:
        print("Result is too large.")

calculator()
