# Define a function for styling the output display
def print_message(message):
    horizontal_border = "=" * 50
    formatted_message = (f"{horizontal_border}\n\n"
                         f"{message.center(50)}\n\n"
                         f"{horizontal_border}")
    print(formatted_message)

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
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Create double.txt file containing squares of even integers
with open("double.txt", "w") as double_file:
    double_file.write("Here are the square of all even integers: \n")
    for num in even_numbers:
        double_file.write(f"{num}\N{SUPERSCRIPT TWO} = {num ** 2} \n")

# Create triple.txt file containing cubes of odd numbers
with open("triple.txt", "w") as triple_file:
    triple_file.write("Here are the cube of all odd integers: \n")
    for num in odd_numbers:
        triple_file.write(f"{num}\N{SUPERSCRIPT THREE} = {num ** 3} \n")

# Shows an output where the files are already created
print_message("The files have been created :>.")