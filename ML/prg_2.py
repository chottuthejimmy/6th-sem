# For a given set of training data examples stored in a .CSV file, 
# implement and demonstrate the Candidate-Elimination algorithm 
# to output a description of the set of all hypotheses consistent with the training examples.

import csv

hypo = []
data = []
temp = []
gen = ['?', '?', '?', '?', '?', '?']

with open('enjoysport.csv') as csv_file:
    fd = csv.reader(csv_file)
    print("\nThe given training examples are:")
    for line in fd:
        print(line)
        temp.append(line)
        if line[-1] == "yes":
            data.append(line)

print("\nThe positive examples are: Enjoy swimming")
for example in data:
    print(example)

print("\nThe final specific output:")

hypo = data[0][:-1]

for example in data:
    for i in range(len(hypo)):
        if example[i] != hypo[i]:
            hypo[i] = '?'
            
print(hypo)

print("\nThe final Generalize output:")

row = len(temp)
col = len(temp)

for i in range(row):
    if temp[i][-1] == "no":
        for j in range(col - 1):
            if temp[i][j] != hypo[j]:
                gen[j] = hypo[j]
                print(gen)
                gen[j] = '?'