print("----- SIMPLE CALCULATOR -----")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nOperations")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose operation (1/2/3/4): ")

if choice == "1":
    print("Result =", num1 + num2)

elif choice == "2":
    print("Result =", num1 - num2)

elif choice == "3":
    print("Result =", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero not allowded")"

else:
    print("Invalid Choice")