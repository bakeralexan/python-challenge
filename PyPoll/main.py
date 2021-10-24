import os
import csv
csv_path = os.path.join("Resources", "election_data.csv")

with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = csvfile.readline()

    unique_list = []
    winner = ""
    candidate_list = []
    khan_list = []
    Correy_list = []
    Li_list = []
    OTooley_list = []
    row = ()

    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        if candidate not in unique_list:
            unique_list.append(candidate)

        candidate_list.append(candidate)

        if candidate == "Khan" :
            khan_list.append(candidate)
        elif candidate == "Correy" :
            Correy_list.append(candidate)
        elif candidate =="Li" :
            Li_list.append(candidate)
        elif candidate == "O'Tooley" :
            OTooley_list.append(candidate)
    print(f" These are the candidates: {unique_list}")
    total_cast = len(candidate_list)
    total_Khan = len(khan_list)
    total_Li = len(Li_list)
    total_Correy = len(Correy_list)
    total_OTooley = len(OTooley_list)

    Khan_percent = "{:.3f}".format((total_Khan/total_cast)*100)
    Correy_percent = "{:.3f}".format((total_Correy/total_cast)*100)
    Li_percent = "{:.3f}".format((total_Li/total_cast)*100)
    OTooley_percent = "{:.3f}".format((total_OTooley/total_cast)*100)

    if total_Khan > total_Correy and total_Khan > total_Li and total_Khan > total_OTooley:
        winner = "Khan"
    elif total_Correy > total_Khan and total_Correy > total_Li and total_Correy > total_OTooley:
        winner = "Correy"
    elif total_Li > total_Khan and total_Li > total_Correy and total_Li > total_OTooley:
        winner = "Li"
    elif total_OTooley > total_Li and total_OTooley > total_Khan and total_OTooley > total_Correy:
        winner = "O'Tooley"

    print("Election Results")
    print(f"CSV: {csv_header}")
    print("----------------------------")
    print(f"Total Votes: {total_cast}")
    print("----------------------------")
    print(f"Khan: {Khan_percent}% ({total_Khan}) votes.")
    print(f"Correy: {Correy_percent}% ({total_Correy}) votes.")
    print(f"Li: {Li_percent}% ({total_Li}) votes.")
    print(f"O'Tooley: {OTooley_percent}% ({total_OTooley}) votes.")
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")