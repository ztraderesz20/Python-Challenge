import os
import csv

#  Define path to data file
election_csv = os.path.join('Resources', 'election_data.csv')

#  Open and read csv data file
with open(election_csv, 'r') as csvfile:
    election_reader = csv.reader(csvfile, delimiter=',')
    header = next(election_reader)
    
    voter_id = []
    candidate = []
    
    for row in election_reader:
        voter_id.append(row[0])
        candidate.append(row[2])

#  Answer.1
total_votes = len(voter_id)

# Answer.2
unique_cand = list(set(candidate))

count_khan = 0
count_li = 0
count_otooley = 0
count_correy = 0

for i in candidate:
    if i == "Khan":
        count_khan = count_khan + 1
    elif i == "Li":
        count_li = count_li + 1
    elif i == "O'Tooley":
        count_otooley = count_otooley + 1
    elif i == "Correy":
        count_correy = count_correy + 1

cand_counts = [count_correy, count_li, count_otooley, count_khan ]

#  Calculate percentages for each candidate
cand_pct = []
for x in cand_counts:
    cand_pct.append(x/total_votes*100)

#  Apply formatting for 3 decimal places    
cand_pct3 = [ '%.3f' % elem for elem in cand_pct ]

#  Combine lists into tuple
zip_list = zip(unique_cand, cand_pct3, cand_counts)

#  Output formatting to terminal
#------------------------------------------------------------------------------------------------
print( 'Election Results')
print('------------------------------------')
print(f'Total Votes:  {total_votes}')
print('------------------------------------')

print(list(zip_list))

#  Output results to data file
#-------------------------------------------------------------------------------------------
election_results_file = os.path.join('output','election_results.csv')
with open(election_results_file, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total Votes:', total_votes])

    