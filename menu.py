"""
    --------MENU ITEMS--------
    1. Multiplication
    2. Division
    3. Addition
    4. Subtraction
    0. Exit/End
    --------------------------
"""
from os import system

def display_menu()->None:
    print("--------MENU ITEMS-------- \n1. Multiplication \n2. Division \n3. Addition \n4. Subtraction \n0. Exit/End \n--------------------------")
    
def intro():
    print("\n")
    display_menu()
    get_option()
    
product = lambda first_value, second_value: first_value * second_value
quotient = lambda first_value, second_value: first_value / second_value
sum = lambda first_value, second_value: first_value + second_value
difference = lambda first_value, second_value: first_value - second_value

def result(choice:int, first_value:int, second_value:int)->int: 
    if choice == 1:
        print("\nThe product of %d and %d is %d" % (first_value,second_value,product(first_value,second_value)))
    elif choice == 2:
        print("\nThe quotient of %.2f and %.2f is %.2f" % (first_value,second_value,quotient(first_value,second_value)))
    elif choice == 3:
        print("\nThe sum of %d and %d is %d" % (first_value,second_value,sum(first_value,second_value)))
    elif choice == 4:
        print("\nThe difference of %d and %d is %d" % (first_value,second_value,difference(first_value,second_value)))
    else:
        print("Invalid Input. Please try again...")
        intro()
        
def get_option()->int:
    first:int
    second:int
    option = int(input("Enter your option: "))
    if option > 0 and option <= 4: #WHAT IF THE ENTERED VALUE IS INVALID, WHAT WOULD THE PROGRAM DO?? ~to be continued
        first_value = int(input("Enter First Value: "))
        second_value = int(input("Enter Second Value: ")) 
        result(option,first_value,second_value)
    elif option == 0:
        print("\nProgram Terminated...")
    else:
        print("\nPlease enter from 0-4 only...")
        intro()
        
def main()->None:
    system("cls")
    display_menu()
    get_option()
    
if __name__ == "__main__":
    main()
