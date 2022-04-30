# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    print(headers)


#to retrieve first row in file reader
   # for row in file readr_reader:
    #    print(row[0])


#get number of registered voters in Arapahoe county
##counties_dict['Arapahoe']

# How many votes did you get?
##my_votes = int(input("How many votes did you get in the election? "))

#Total votes in the election
##total_votes = int(input("What is the total votes in the election? "))

#Calculate the percentage of votes you received.
##percentage_votes = (my_votes / total_votes) * 100
##print("I received " + str(percentage_votes)+"% of the total votes.")
