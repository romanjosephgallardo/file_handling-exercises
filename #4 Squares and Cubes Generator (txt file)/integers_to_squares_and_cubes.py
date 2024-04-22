# Define a function for styling the output display
def print_message(message):
    horizontal_border = "=" * 50
    formatted_message = (f"{horizontal_border}\n\n"
                         f"{message.center(50)}\n\n"
                         f"{horizontal_border}")
    print(formatted_message)


# Calculate square of even numbers
def square_integers(num):
    square = num ** 2
    return "{:,.0f}".format(square)


# Calculate cube of odd numbers
def cube_integers(num):
    cube = num ** 3
    return "{:,.0f}".format(cube)


# Read the contents of the source text file
try:
    with open("integers.txt", "r") as file:
        integers_str = file.read().split()
        # Convert string to integers, handling non-integer values
        integers = []
        for int_str in integers_str:
            try:
                num = int(int_str)
                integers.append(num)
            except ValueError:
                print_message(f"Error: non-integer value found in file.")
                exit(1)
except FileNotFoundError:
    print_message("Error: File not found.")
    exit(1)

# Find the even and odd numbers in the txt file
even_numbers = []
odd_numbers = []

for num in integers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Create double.txt file containing squares of even integers
with open("double.txt", "w") as double_file:
    double_file.write("Here are the square of all even integers: \n")
    for num in even_numbers:
        double_file.write(f"{num}\N{SUPERSCRIPT TWO} = {square_integers(num)} \n")

# Create triple.txt file containing cubes of odd numbers
with open("triple.txt", "w") as triple_file:
    triple_file.write("Here are the cube of all odd integers: \n")
    for num in odd_numbers:
        triple_file.write(f"{num}\N{SUPERSCRIPT THREE} = {cube_integers(num)} \n")

# Shows an output where the files are already created
print_message("The files have been created :>.")
