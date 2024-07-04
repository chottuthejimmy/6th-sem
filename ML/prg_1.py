import csv


data = []

# Read the CSV file
with open('enjoysport.csv') as csv_file:
    fd = csv.reader(csv_file)
    print("\nThe given training examples are:")
    for line in fd:
        print(line)
        if line[-1] == "yes":
            data.append(line)

print("\nThe positive examples are:")
for example in data:
    print(example)


# Initialize hypo with the first positive example
hypo = data[0][:-1]

# Find-S algorithm
print("\nThe steps of the Find-S algorithm are:")
print(hypo)
for example in data[1:]:
    for i in range(len(hypo)):
        if example[i] != hypo[i]:
            hypo[i] = '?'
    print(hypo)

print("\nThe maximally specific Find-S hypo for the given training examples is:")
print(hypo)

