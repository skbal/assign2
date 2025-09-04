# Ask for user input
text = input("Enter a string: ")
char = input("Enter the character to count: ")

# Check if the input is a single character
if len(char) != 1:
    print("Please enter exactly one character.")
else:
    # Count and print the frequency
    frequency = text.count(char)
    print(f"The character '{char}' appears {frequency} time(s) in the string."
