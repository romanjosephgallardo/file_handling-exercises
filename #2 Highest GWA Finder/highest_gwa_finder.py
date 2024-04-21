# pseudocode

# Have a file with 20 students and their GWA (done)

# Read the file
import pandas as pd
students_gwa = pd.read_excel("students_gwa.xlsx")

# Find the student with highest GWA
# Sorts the GWA (1.00 being the highest)
highest_to_lowest = (
    students_gwa
    .sort_values("GWA", ascending=True)
    .to_string(index=False)
)

# Locate the first row
highest_gwa_row = (highest_to_lowest.split("\n")[1])

# Split the row into individual elements
elements = highest_gwa_row.split()

# Declaring the second and third element
name = " ".join(elements[:-1])
gwa = elements[-1]

# Display the student and their GWA
