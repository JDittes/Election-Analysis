#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
dir(csv)
dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})
dir(str)
dir(int)
dir(float)
dir(bool)
dir(list
)
dir(tuple)
dir(dict)
#dir(daetime)
#dir(random)
dir(dt)

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

import csv
import os
dir(os)
dir(os.path)
os.path.join("Resources", "election_results.csv")
file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
 # Write three counties to the file.
outfile.write("Arapahoe\nDenver\nJefferson")

# Close the file
outfile.close()

