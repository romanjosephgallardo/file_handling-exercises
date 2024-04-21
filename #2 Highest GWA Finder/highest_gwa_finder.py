# pseudocode

# Have a file with 20 students and their GWA (done)

def print_message(message, another_message):
    horizontal_border = "=" * 50
    formatted_message = (f"{horizontal_border}\n\n"
                        f"{message.center(50)}\n"
                        f"{another_message.center(50)}\n\n"
                        f"{horizontal_border}")
    print(formatted_message)


# Read the file
import pandas as pd

student_data = pd.read_excel("students_gwa.xlsx")

# Find the student with highest GWA
highest_gwa = student_data.loc[student_data['GWA'].idxmin()]

# Extract the name and GWA of the student
student_name = highest_gwa.iloc[0]
student_gwa = highest_gwa.iloc[1]

# Display the student and their GWA
output_message = "Student with the highest GWA:"
name_and_gwa = f"{student_name} — {student_gwa}"
print_message(output_message, name_and_gwa)
