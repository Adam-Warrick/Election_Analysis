file_to_load = 'Resources/election_results.csv'
with open(file_to_load) as election_data:
    print(election_data)

import os
import csv

file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
    txt_file.write("Hi")
    
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    for row in file_reader:
        print(row)




