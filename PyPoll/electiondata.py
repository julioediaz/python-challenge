import csv

#Import CSV file
csvpath ="election_data_2.csv"
results_file = "election_results.txt"

#list to store votes
new_candidate = {}

#Open the CSV.

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Loop through rows
    #The total number of votes cast
    #vote counter
    voter_count = 0
    for row in csvreader:

        voter_count += 1
        candidate = row[2]

        if (candidate != "Candidate"):
            if (candidate not in new_candidate):
                new_candidate[row[2]] = 1
            else:
                new_candidate[row[2]] += 1

winner_votes = 0
winner_name = ""

with open(results_file, "w") as txt_file:

    header = ("Election Results \n"
        "-----------------------\n"
        "Total Votes: " + str(voter_count) + "\n"\
        "-----------------------\n")

    txt_file.write(header)
    print(header)

    for candidate, votes in new_candidate.items():
        if votes > winner_votes:
            winner_name = candidate
            winner_votes = votes
        vote_percentage = (float(votes)/float(voter_count))*100
        vote_percentage = round(vote_percentage, 2)
        print(candidate + ": " + str(vote_percentage) + "% (" + str(votes) + ")")
        txt_file.write(candidate + ": " + str(vote_percentage) + "% (" + str(votes) + ")")
    print("-----------------------")
    print("Winner: " + winner_name)
    txt_file.write("Winner: " + winner_name)
    print("-----------------------")

