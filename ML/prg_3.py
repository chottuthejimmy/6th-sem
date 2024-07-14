# Write a program to demonstrate the working of the decision tree based ID3 algorithm.
# Use an appropriate data set for building the decision tree 
# and apply this knowledge to classify a new sample.

import csv
from math import log2

def get_data(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)
        for line in data:
            print(line)
    return data[1:], data[0]

def entropy(data):
    outcomes = [row[-1] for row in data]
    probs = [outcomes.count(value) / len(outcomes) for value in set(outcomes)]
    return -sum(p * log2(p) for p in probs)

def split_data(data, attr):
    values = set(row[attr] for row in data)
    return [[row for row in data if row[attr] == value] for value in values]

def best_attribute(data):
    base_entropy = entropy(data)
    gain = [(base_entropy - sum((len(subset) / len(data)) * entropy(subset) for subset in split_data(data, attr)), attr) for attr in range(len(data[0]) - 1)]
    return max(gain)[1]

def decision_tree(data, labels):
    outcomes = [row[-1] for row in data]
    if outcomes.count(outcomes[0]) == len(outcomes):
        return outcomes[0]
    attr = best_attribute(data)
    tree = {labels[attr]: {}}

    for value in set(row[attr] for row in data):
        sub_labels = labels[:attr] + labels[attr+1:]
        sub_data = [row[:attr] + row[attr+1:] for row in data if row[attr] == value]

        tree[labels[attr]][value] = decision_tree(sub_data, sub_labels)
        
    return tree

data, labels = get_data("weather.csv")
tree = decision_tree(data, labels)
print("\nDecision Tree:", tree)