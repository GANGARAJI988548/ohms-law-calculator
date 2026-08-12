print("ELECTRICAL POWER CALCULATOR")
print("Formulas: P = V × I, V = P / I, I = P / V")

choice = input("What do you want to calculate? (P/V/I): ").upper()

if choice == "P":
    V = float(input("Enter voltage (V): "))
    I = float(input("Enter current (A): "))
    P = V * I
    print("Power =", P, "W")

elif choice == "V":
    P = float(input("Enter power (W): "))
    I = float(input("Enter current (A): "))
    V = P / I
    print("Voltage =", V, "V")

elif choice == "I":
    P = float(input("Enter power (W): "))
    V = float(input("Enter voltage (V): "))
    I = P / V
    print("Current =", I, "A")

else:
    print("Invalid choice")
