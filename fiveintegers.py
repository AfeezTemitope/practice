numbers = input("Enter a five-digit integer: ")
if len(numbers) != 5 or not numbers.isdigit():
    print("Please enter a valid five-digit integer.")
else:
    for digit in numbers:
        print(digit, end="\n") 