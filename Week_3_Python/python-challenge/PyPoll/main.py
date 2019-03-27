import os
import csv

# Import collections (for counter_for_whileloop , dictionary)
import collections

# Create output text file
text_file = open("output_pypoll.txt", "w")

# Create path for file
PypollDatacsv = os.path.join('.','Resource','homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

# Declare variables to store data in arrays
candidates_unique =[]
list_to_find_winner = []
votes = []

# Declare variables
total_votes = 0
counter_for_whileloop= 0


# Read in the CSV file
with open(PypollDatacsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # first row is header
    header = next(csvreader)

# Loop through the data
    for row in csvreader:
        total_votes = int(total_votes) + 1

    # get unique candidate names from the data set and append the names into the candidates_unique list
        if row[2] not in candidates_unique :
            candidates_unique.append(row[2])

        # Append each vote to votes list
        votes.append(row[2])


# Print results as text file
text_file.write("Election Results\n------------------------\n")  
text_file.write(f"Total Votes: {total_votes}\n")
text_file.write("------------------------\n")

# Print results at terminal
print(" Election Results\n------------------------")
print(f" Total Votes: {total_votes}")
print("------------------------\n")

# Set counter(counter_for_whileloop) to be the length of the candidates (candidates_unique) list. -1 is applied becuase first index = 0
counter_for_whileloop = len(candidates_unique) - 1 

# Create a dictonary with name of candidates are the keys and the number of votes are values
dictionary = collections.Counter(votes)

# whileloop 
while counter_for_whileloop != -1:

 
    # Value from the dictonary for candidate index counter_for_whileloop.
    variable_from_dictionary = dictionary.get(candidates_unique[counter_for_whileloop], None)
    print(f"{candidates_unique[counter_for_whileloop]}: {(variable_from_dictionary * 100) / total_votes}% ({str(variable_from_dictionary)})")
    
 

    # Print results as text file
    text_file.write(f"{candidates_unique[counter_for_whileloop]}: {(variable_from_dictionary*100)/total_votes}% ({str(variable_from_dictionary)})\n")
    list_to_find_winner.append(variable_from_dictionary)
    counter_for_whileloop = counter_for_whileloop - 1

# Reverse list conatining the count of votes per candidate in order to match indexes from the candidate list. 
# Need both lists to match index for calculating the winner.
list_to_find_winner.reverse()



# Print the Winner by using the max function in the list_to_find_winner.
# the list_to_find_winner contains each of the total values each candidate in the same order as the candidate list. 
# Getting the index of the highest value can be used as the index for the candidates list to identify the name of the winner candidate
print("------------------------")
print(f" Winner: {candidates_unique[list_to_find_winner.index(max(list_to_find_winner))]}")
print("------------------------")

# Print result into output text file
text_file.write(f"-------------------\n")
text_file.write(f" Winner: {candidates_unique[list_to_find_winner.index(max(list_to_find_winner))]}")
text_file.write(f"-------------------\n")


# Close output text file
text_file.close()