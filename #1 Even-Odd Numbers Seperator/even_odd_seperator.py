# pseudocode

# Make a "numbers.txt" file with 20 integers

# Read the contents of the txt file
with open("numbers.txt", "r") as file:
    numbers = file.read().split()

# Convert string to integers
    numbers = (int(num) for num in numbers)

# Find the even and odd numbers in the list
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Create an "even.txt" for even numbers
# Create an "odd.txt" for odd numbers
