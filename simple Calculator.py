
print("Simple Calculator")
attempts = 0
def add():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f" The Result is {result}")
    except ValueError:
        print("enter only numbers")

def subtract():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print(f" The result is {result}")
    except ValueError:    
        print("enter only numbers")


def multiplication():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print(f" The result is {result}")
    except ValueError:
        print("enter only numbers")
def division():
    try:
        num1 = float(input("enter the number: "))  
        num2 = float(input("enter the number: "))
    except ValueError:
        print("enter only numbers")
    try:
              result = num1 / num2
              print(f"  The result is {result}") 
    except ZeroDivisionError:
                print("Error: Division by zero is not allowed.") 

def menu():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter choice (1/2/3/4): ")
    if choice == '1':
        add()
    elif choice == '2':
        subtract()
    elif choice == '3':
        multiplication()
    elif choice == '4':
        division()
    elif choice == '5':
         print("Existing the calculator; GOODBYE!")
         return 0
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
while (attempts < 5):
 menu()
attempts += 1
    
      

                           
