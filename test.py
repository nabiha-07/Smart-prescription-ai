# A simple beginner-friendly Python program.

print("Hello! Claude Code is working.")

# Ask for the user's name and greet them.
name = input("What is your name? ")
print("Nice to meet you, " + name + "!")

# Ask for two numbers and add them together.
first = input("Enter the first number: ")
second = input("Enter the second number: ")

try:
    total = float(first) + float(second)
    print("The sum of " + first + " and " + second + " is " + str(total))
except ValueError:
    print("Sorry, that was not a valid number. Please run the program again.")
