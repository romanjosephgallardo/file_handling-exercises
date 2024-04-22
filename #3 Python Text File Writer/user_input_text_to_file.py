# pseudocode

# Create a text file
with open("mylife.txt", "w") as file:

# Prompt user to input a line of text
    line = input("Enter line: ")
    file.write(line + "\n")

# Ask user where there are more lines to enter
    more_lines = input("Are there more lines? (y/n): ")
    if more_lines.lower() != "y":

# If no more lines, end the program.
        print("Contents written to mylife.txt successfully! :>")
