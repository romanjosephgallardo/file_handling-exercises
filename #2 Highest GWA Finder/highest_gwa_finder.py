# pseudocode

# Have a file with 20 students and their GWA (done)

# Read the file
import pandas as pd
students_gwa = pd.read_excel("students_gwa.xlsx")

# Find the student with highest GWA
highest_to_lowest = (
    students_gwa
    .sort_values("GWA", ascending=True)
    .to_string(index=False)
) # Sorts the GWA (1.00 being the highest)
highest_gwa_row = (highest_to_lowest.split("\n")[1])




# Display the student and their GWA
