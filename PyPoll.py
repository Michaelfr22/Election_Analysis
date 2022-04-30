# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

####INITIALIZE

# accumulator
total_votes = 0

#candidate options
candidate_options = []

#candidate votes
candidate_votes = {}

#winning candidate tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    
    #print each row in the CSV file.
    for row in file_reader:
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #if candidate name does not yet exist
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #begin tracking candidate votes; vote counter should be outside FOR LOOP
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1


# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = round(float(votes) / float(total_votes) * 100)

    #to do: print out each candidate's name, vote count, and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine winning vote count and candidate
    
    #determine if the votes is greater than the winning count

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

#candidate summary    
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
