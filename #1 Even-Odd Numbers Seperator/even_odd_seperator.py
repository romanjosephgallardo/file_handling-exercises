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
with open("even.txt", "w") as even_file:
    even_file.write("Here is the even numbers: \n")
    for num in even_numbers:
        even_file.write(str(num) + "\n")

# Create an "odd.txt" for odd numbers
with open("odd.txt", "w") as odd_file:
    odd_file.write("Here is the odd numbers: \n")
    for num in odd_numbers:
        odd_file.write(str(num) + "\n")