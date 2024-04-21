# pseudocode

# Have a file with 20 students and their GWA (done)

# Read the file
import pandas as pd
student_data = pd.read_excel("students_gwa.xlsx")

# Find the student with highest GWA
highest_gwa = student_data.loc[student_data['GWA'].idxmin()]

# Extract the name and GWA of the student
student_name = highest_gwa.iloc[0]
student_gwa = highest_gwa.iloc[1]

# Display the student and their GWA
print("Student with the highest GWA:")
print(f"Name: {student_name}")
print(f"GWA: {student_gwa}")