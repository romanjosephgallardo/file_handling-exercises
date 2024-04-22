# pseudocode

# Create a text file
with open("mylife.txt", "w") as file:
    while True:
        # Prompt user to input a line of text
        line = input("Enter line: ")
        if not line.strip():  # Check if line is empty or whitespace only
            print("Invalid line. Please enter a non-empty line.")
            continue
        file.write(line + "\n")

        while True:
            # Ask user where there are more lines to enter
            more_lines = input("Are there more lines? (y/n): ")
            if more_lines.lower() == "y" or more_lines.lower() == "n":
                break
            else:  # Prompts the user for invalid input
                print("Invalid input. Please enter 'y' or 'n' only.")
        # If no more lines, end the program.
        if more_lines.lower() == "n":
            print("Contents written to file successfully! :>")
            break
