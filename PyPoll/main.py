import os
import csv

#initializing variables
total_number_of_votes = 0
candidates = [] # to store name of candidates
votes_per_candidate = [] # to store number of votes each candidate got also note that the candidate and his/her votes fall in the same index
winner = ""
winner_percentage = 0


#get path of path and open it
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, "r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #read the first line alone since it contains the headers
    first_row = next(csvreader)
    #loop over the data in the file
    for row in csvreader:
        total_number_of_votes = total_number_of_votes + 1 #count number of rows
        # if candidate already exists then we increase his/her number of votes by one
        if row[2] in candidates:
            votes_per_candidate[candidates.index(row[2])] = votes_per_candidate[candidates.index(row[2])] + 1
        #if we have a new candidate then we append his/her to the candidates list and give him 1 vote
        else:
            candidates.append(row[2])
            votes_per_candidate.append(1)

#create a text file
output_file = os.path.join("analysis", "results.txt")

#open the text file, write in it, and print in the terminal
with open(output_file, "w", encoding="utf-8") as datafile:
    writer = csv.writer(datafile) 
    writer.writerow([str("Election Results")])
    print("Election Results")
    writer.writerow([str("----------------------------")])
    print("----------------------------")
    x = "Total Votes: " + str(total_number_of_votes)
    writer.writerow([str(x)])
    print(x)
    writer.writerow([str("----------------------------")])
    print("----------------------------")
    for candidate in candidates:
        percent = round(votes_per_candidate[candidates.index(candidate)]/total_number_of_votes * 100, 2)
        x = candidate + ": " + '{:.3f}'.format(percent) + "%(" + str(votes_per_candidate[candidates.index(candidate)]) + ")"
        writer.writerow([str(x)])
        print(x)
        #using this if state to look for the candidate with the highest vote percentage
        if winner_percentage < percent:
            winner_percentage = percent
            winner = candidate
    writer.writerow([str("----------------------------")])
    print("----------------------------")
    x = "Winner: " + winner
    writer.writerow([str(x)])
    print(x)
    writer.writerow([str("----------------------------")])
    print("----------------------------")

    
  
