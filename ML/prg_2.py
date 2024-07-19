# For a given set of training data examples stored in a .CSV file, 
# implement and demonstrate the Candidate-Elimination algorithm 
# to output a description of the set of all hypotheses consistent with the training examples.

import csv

data = []
temp = []

with open('enjoysport.csv') as csv_file:
    fd = csv.reader(csv_file)
    print("\nThe given training examples are:")
    for line in fd:
        print(line)
        temp.append(line)
        if line[-1] == "yes":
            data.append(line)

gen = ['?' for _ in range(len(data[0]))]

print("\nThe positive examples are: ")
for example in data:
    print(example)

hypo = data[0][:-1]

for example in data[1:]:
    for i in range(len(hypo)):
        if example[i] != hypo[i]:
            hypo[i] = '?'
            
print(f"\nThe final specific output:\n{hypo}")

print("\nThe final Generalize output:")

for example in temp:
    if example[-1] == "no":
        for i in range (len(hypo)):
            if example[i] != hypo[i]:
                gen[i] = hypo[i]
                print(gen)
                gen[i] = '?'