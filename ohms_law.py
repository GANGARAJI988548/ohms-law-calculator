print("OHM'S LAW CALCULATOR")
print("V = I × R")

choice = input("What do you want to calculate? (V/I/R): ").upper()

if choice == "V":
    I = float(input("Enter current (A): "))
    R = float(input("Enter resistance (Ω): "))
    V = I * R
    print("Voltage =", V, "V")

elif choice == "I":
    V = float(input("Enter voltage (V): "))
    R = float(input("Enter resistance (Ω): "))
    I = V / R
    print("Current =", I, "A")

elif choice == "R":
    V = float(input("Enter voltage (V): "))
    I = float(input("Enter current (A): "))
    R = V / I
    print("Resistance =", R, "Ω")

else:
    print("Invalid choice")
