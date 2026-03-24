"""
Filename: average_calculator.py
Author: <NAME>
Created: <DATE>
Instructor: Holtslander
"""

# Create a list to store numbers here
while True:
    op = input("Please select your desired operation by typing the number, then pressing \"enter\"\n"
               "Fill out the rest of the options here\n"
               "\n"
               "\n"
               "\n"
               "5) Exit the program. !WARNING! all data will be erased!\n")

    # Create the conditional statements and the code associated with them for the rest of the options here

    elif op == "5":
        break
    else:
        print(f"{op} is not a supported operation! Try again.")
print("Thank you for using this average calculator!")


