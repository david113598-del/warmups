"""
Filename: simple_primality.py
Author: <david H>
Created: <2/27/26>
Instructor: Holtslander
"""

def prime():
            # Write your code here
    n = int(input("please put in a non negative whole number, its gotta be more than 1.  \n"))
    j = n > n
    if j == 1 or n:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")


# You should not need to change any code below this point
def main():
    print("This program will determine the primality of a number.")
    running = "y"
    while running == "y":
        prime()
        running = input("Check another number? (y/N)\n").lower()
    print("Thank you for using this primality program!")

if __name__ == "__main__":
    main()