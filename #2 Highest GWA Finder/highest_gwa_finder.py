import pandas as pd

""" Have a file with 20 students and their GWA.
For this program, it uses Excel file (.xlsx).
It uses a 5-point scale for GWA, with 1.00 being the highest
"""


# Define a function to print an output
def print_message(first_line, second_line):
    horizontal_border = "=" * 50
    formatted_message = (f"{horizontal_border}\n\n"
                         f"{first_line.center(50)}\n"
                         f"{second_line.center(50)}\n\n"
                         f"{horizontal_border}")
    print(formatted_message)


# Define a function to print error outputs
def print_error_message(error):
    horizontal_border = "=" * 50
    formatted_message = f"{horizontal_border}\n\n{error.center(50)}\n\n{horizontal_border}"
    print(formatted_message)


# Read the file and handle errors
try:
    student_data = pd.read_excel("students_gwa.xlsx")
except FileNotFoundError:
    print_error_message("Error: File not found.")
    exit(1)

# Check if the file is empty
if student_data.empty:
    print_error_message("Error: No data found in the file")

# Find the student with highest GWA
highest_gwa = student_data.loc[student_data['GWA'].idxmin()]

# Extract the name and GWA of the student
student_name = highest_gwa.iloc[0]
student_gwa = highest_gwa.iloc[1]

# Display the student and their GWA
output_message = "Student with the highest GWA:"
name_and_gwa = f"{student_name} — {student_gwa}"

print_message(output_message, name_and_gwa)
