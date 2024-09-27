def calculate_voltage(current, resistance):
    return current * resistance

def calculate_current(voltage, resistance):
    if resistance == 0:
        return "Error: Resistance cannot be zero for current calculation."
    return voltage / resistance

def calculate_resistance(voltage, current):
    if current == 0:
        return "Error: Current cannot be zero for resistance calculation."
    return voltage / current

def main():
    while True:
        # Ask the user what they want to calculate
        print("What do you want to calculate?")
        print("1. Voltage")
        print("2. Current")
        print("3. Resistance")
        choice = int(input("Enter 1, 2, or 3: "))

        # Perform the appropriate calculation based on user's choice
        if choice == 1:
            current = float(input("Enter the current (in amperes): "))
            resistance = float(input("Enter the resistance (in ohms): "))
            voltage = calculate_voltage(current, resistance)
            print(f"The voltage is {voltage} volts.")
        elif choice == 2:
            voltage = float(input("Enter the voltage (in volts): "))
            resistance = float(input("Enter the resistance (in ohms): "))
            current = calculate_current(voltage, resistance)
            print(f"The current is {current} amperes.")
        elif choice == 3:
            voltage = float(input("Enter the voltage (in volts): "))
            current = float(input("Enter the current (in amperes): "))
            resistance = calculate_resistance(voltage, current)
            print(f"The resistance is {resistance} ohms.")
        else:
            print("Invalid choice. Please try again.")

        # Ask the user if they want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != 'yes':
            break

# Entry point of the program
if __name__ == "__main__":
    main()
