# pseudocode

# Read the contents of the source text file
with open("integers.txt", "r") as file:
    integers = file.read().split()
    # Convert string to integers
    integers = (int(num) for num in integers)

# Find the even and odd numbers in the txt file
even_numbers = []
odd_numbers = []

for num in integers:
    if num % 2 == 0:
        squared_numbers = num ** 2
    else:
        cubed_numbers = num ** 3

# Create double.txt file containing squares of even integers
# Create triple.txt file containing cubes of odd numbers
# Shows an output where the files are already created
