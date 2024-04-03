
# Input a five-digit integer from the user
user_input = input("Enter a five-digit integer: ")

# Check if the input is a valid five-digit integer
if user_input.isdigit() and len(user_input) == 5:
    # Separate the digits and print them with three spaces in between
    print(*user_input, sep="   ")
else:
    print("Invalid input. Please enter a valid five-digit integer.")