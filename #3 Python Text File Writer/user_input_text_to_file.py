# Define a function for horizontal line
def horizontal_border():
    print("=" * 50, "\n")


# Define a function for printing specific outputs
def print_message(message):
    formatted_output = f">> {message}"
    print(formatted_output)


horizontal_border()  # Calls the horizontal border function

# Create a text file
with open("mylife.txt", "w") as file:
    while True:
        # Prompt user to input a line of text
        line = input("Enter line: ")
        if not line.strip():  # Check if line is empty or whitespace only
            print_message("Invalid line. Please enter a non-empty line.")
            continue
        file.write(line + "\n")

        while True:
            # Ask user where there are more lines to enter
            more_lines = input("Are there more lines? (y/n): ")
            if more_lines.lower() == "y" or more_lines.lower() == "n":
                break
            else:  # Prompts the user for invalid input
                print_message("Invalid input. Please enter 'y' or 'n' only.")
        # If no more lines, end the program.
        if more_lines.lower() == "n":
            print_message("Contents written to file successfully! :> \n")
            break

horizontal_border()
