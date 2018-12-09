import os
import csv

candidate_dict =    {"name":[],
                     "vote_count":[],
                     "percent":[],
                     "display":[]
                    }
total_votes = 0
csv_path = "../Resources/election_data.csv"
with open (csv_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    # Bypassing the header record
    header=next(csv_reader)
    #print(header)
    for row in csv_reader:
        total_votes += 1
        voter_id = row[0]
        county = row[1]
        candidate = row [2]
        if candidate not in candidate_dict["name"]:
            #create the details in the list and append the values to be calculated with initial values
            #print(f'{candidate} not in list')
            candidate_dict["name"].append(candidate)
            candidate_dict["vote_count"].append(int(1))
            candidate_dict["percent"].append(0.00)
            candidate_dict["display"].append('')
            #print(f'Adding it {candidate_dict}')
        else:
            #Update the count for existing candidates
            idx_position = candidate_dict["name"].index(candidate)
            count = candidate_dict["vote_count"][idx_position]
            count += 1
            candidate_dict["vote_count"][idx_position] = count

winner_percent = 0.00
calc_percent = 0.00
winner_name = ''
for each_cand in candidate_dict["name"]:
    # calculating the percentages and creating the display lines
    idx_position = candidate_dict["name"].index(each_cand)
    calc_percent = (candidate_dict["vote_count"][idx_position]/total_votes) * 100
    candidate_dict["percent"][idx_position] = calc_percent
    candidate_dict["display"][idx_position] = str(candidate_dict["name"][idx_position]) + ":" + str(candidate_dict["percent"][idx_position]) + "% (" + str(candidate_dict["vote_count"][idx_position]) + ")"
    if winner_percent < calc_percent:
        winner_name = candidate_dict["name"][idx_position]
        winner_percent = calc_percent

winner_string = "Winner is : " + str(winner_name)

#print(f'After calculating the percentage: {candidate_dict}')
#print(f'Total Number of votes: {total_votes}')

Display_line1 = "Election Results"
Display_line = '---------------------'

output_path = "../Resources/election_results.txt"
with open (output_path, 'w') as outfile:
    print(Display_line)
    outfile.write(Display_line)
    outfile.write('\n')
    print(Display_line1)
    outfile.write(Display_line1)
    outfile.write('\n')
    print(Display_line)
    outfile.write(Display_line)
    outfile.write('\n')

    for each_cand in candidate_dict["name"]:
        idx_position = candidate_dict["name"].index(each_cand)
        print(candidate_dict["display"][idx_position])
        outfile.write(candidate_dict["display"][idx_position])
        outfile.write('\n')

    print(Display_line)
    outfile.write(Display_line)
    outfile.write('\n')
    print(winner_string)
    outfile.write(winner_string)
    outfile.write('\n')
    print(Display_line)
    outfile.write(Display_line)

    
    