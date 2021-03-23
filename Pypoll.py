
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.

# 1. Initialize a total vote counter.
total_votes = 0
candidate_options = []

with open(file_to_load) as election_data:


    # To do: read and analyze the data here.

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #for row in file_reader:
    #    print(row)

    #Print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        #total_votes += 1
        # 3. Print the total votes.
        #print(total_votes, row)
        # Print the candidate name from each row
        candidate_name = row[2]
        # Add the candidate name to the candidate list.
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            

# Print the candidate list.
print(candidate_options)










# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:


# Write some data to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")