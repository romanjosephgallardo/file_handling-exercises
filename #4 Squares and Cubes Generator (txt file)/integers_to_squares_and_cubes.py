# pseudocode

# Read the contents of the source text file
with open("integers.txt", "r") as file:
    integers = file.read().split()
    # Convert string to integers
    integers = (int(num) for num in integers)

# Create double.txt file containing squares of even integers
# Create triple.txt file containing cubes of odd numbers
# Shows an output where the files are already created
