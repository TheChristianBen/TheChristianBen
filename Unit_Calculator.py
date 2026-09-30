def unit_calculator():
    print("Unit Converter")
    print("Select ONE of the categories below: ")
    print("1. Length (Meters<-->Kilometers)")
    print("2. Weights (Grams<-->Kilograms)")
    print("3. Temperature (Celsius<-->Fahrenheit)")

    choice = input("Enter your choice(1/2/3): ")

    try:
        if choice == "1":
            print("\nLength Converter:")
            print("1. Meters to Kilometers")
            print("2. Kilometers to Meters")
            length_choice = input("Which Option Do you want? ")

            if length_choice == "1":
                meters = float(input("Enter value in meters: "))
                kilometers = meters/1000
                print(f"{meters} meters = {kilometers:.4f} kilometers")
            elif length_choice == "2":
                kilometers = float(input("Enter value in Kms: "))
                meters = kilometers * 1000
                print(f"{kilometers} km(s) = {meters:.4f} meters")
            else:
                print("Invalid option for length conversion.")

        elif choice == "2":
            print("\nWeight Converter:")
            print("1. Grams to Kilograms")
            print("2. Kilograms to Grams")
            weight_choice = input("Which Option Do you want? ")

            if weight_choice == "1":
                grams = float(input("Enter value in Grams: "))
                kilograms = grams/1000
                print(f"{grams} grams = {kilograms:.4f} kilograms")
            elif weight_choice == "2":
                kilograms = float(input("Enter value in kgs: "))
                grams = kilograms * 1000
                print(f"{kilograms} kg(s) = {grams:.4f} grams")
            else:
                print("Invalid option for weight conversion.")

        elif choice == "3":
            print("\nTemperature Converter:")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            temp_choice = input("Which Option Do you want? ")

            if temp_choice == "1":
                Celsius = float(input("Enter value in Celsius: "))
                Fahrenheit = (9/5 * Celsius) + 32
                print(f"{Celsius}°C = {Fahrenheit:.2f}°F")
            elif temp_choice == "2":
                Fahrenheit = float(input("Enter value in Fahrenheit: "))
                Celsius = (Fahrenheit - 32) * 5/9
                print(f"{Fahrenheit}°F = {Celsius:.2f}°C")
            else:
                print("Invalid option for temperature conversion.")

        else:
            print("Invalid category choice.")

    except ValueError:
        print("Please enter a valid number.")


unit_calculator()
