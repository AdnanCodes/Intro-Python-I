# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def checkEven(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
checkEven(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE
