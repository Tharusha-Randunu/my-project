def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid choice. Please select a valid operation.")

calculator()
print("Calculator ran successfully!")

