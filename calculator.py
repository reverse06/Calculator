#To quit the program when needed
import sys



# Define the operations
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"



# Function to display ASCII frame
def print_ascii_frame():
    print("+---------------------------------------+\n
    |        Welcome to your Calculator!    |\n
    +---------------------------------------+")



# Main loop

main = True

while main:
    print_ascii_frame()  # Display ASCII frame



    # Display operation choices
    print("Choose an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Quit")


    # Ask user for operation choice
    choix = input("Enter the number for the desired operation (1/2/3/4/5): ")


    # Check if the choice is valid
    if choix == '5':
        print("\nThank you for using the calculator! Goodbye.")
        sys.exit()  # Exit the program
    elif choix in ['1', '2', '3', '4']:
        try:
            a = float(input("\nEnter the first number: "))
            b = float(input("Enter the second number: "))


            # Execute chosen operation
            if choix == '1':
                result = addition(a, b)
                print(f"\nThe result of the addition is: {result}")
            elif choix == '2':
                result = soustraction(a, b)
                print(f"\nThe result of the subtraction is: {result}")
            elif choix == '3':
                result = multiplication(a, b)
                print(f"\nThe result of the multiplication is: {result}")
            elif choix == '4':
                result = division(a, b)
                print(f"\n{result}")


            # Ask if user wants to perform another operation
            continue_choice = input("\nDo you want to perform another operation? (y/n): ").lower()
            if continue_choice != 'y':
                print("\nThank you for using the calculator! Goodbye.")
                sys.exit()  # Exit the program


        except ValueError:
            print("\nError: Please enter valid numbers.")

    else:
        print("\nInvalid choice. Please enter a number between 1 and 4 for operations or 5 to quit.")
