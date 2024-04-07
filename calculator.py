class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

def main():
    calc = Calculator()
    print("Welcome to Calculator App")

    while True:
        print("\nCalculator Operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print("Result:", calc.add(num1, num2))
                elif choice == '2':
                    print("Result:", calc.subtract(num1, num2))
                elif choice == '3':
                    print("Result:", calc.multiply(num1, num2))
                elif choice == '4':
                    print("Result:", calc.divide(num1, num2))
            except ValueError:
                print("Invalid input! Please enter numbers.")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero!")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
