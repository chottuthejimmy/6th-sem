# Write a program to implement the naive Bayesian classifier 
# for a sample training data set stored as a .CSV file. 
# Compute the accuracy of the classifier, considering few test data sets.

import csv
import random
import math
from collections import defaultdict

def load_csv(filename):
    with open(filename, 'r') as file:
        next(file)  # Skip the first row
        return [list(map(float, row)) for row in csv.reader(file)]

def train_test_split(dataset, split_ratio=0.87):
    train_size = int(len(dataset) * split_ratio)
    train_set = random.sample(dataset, train_size)
    test_set = [x for x in dataset if x not in train_set]
    return train_set, test_set

def summarize_by_class(dataset):
    separated = defaultdict(list)
    for row in dataset:
        separated[row[-1]].append(row[:-1])
    
    summaries = {}
    for class_value, instances in separated.items():
        summaries[class_value] = [(sum(attr)/len(attr), math.sqrt(sum((x-sum(attr)/len(attr))**2 for x in attr)/(len(attr)-1))) for attr in zip(*instances)]
    return summaries

def calculate_probability(x, mean, stdev):
    exponent = math.exp(-((x-mean)**2 / (2 * stdev**2)))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent

def predict(summaries, input_vector):
    probabilities = {
        class_value: math.prod(calculate_probability(x, mean, stdev) for x, (mean, stdev) in zip(input_vector, class_summaries)) for class_value, class_summaries in summaries.items()
    }
    return max(probabilities, key=probabilities.get)

def get_accuracy(test_set, predictions):
    correct = sum(test_row[-1] == pred for test_row, pred in zip(test_set, predictions))
    return (correct / len(test_set)) * 100.0

def main():
    filename = 'diabetes.csv'
    dataset = load_csv(filename)
    train_set, test_set = train_test_split(dataset)
    print(f"Split {len(dataset)} rows into training={len(train_set)} and testing={len(test_set)} rows")
    
    summaries = summarize_by_class(train_set)
    predictions = [predict(summaries, row[:-1]) for row in test_set]
    accuracy = get_accuracy(test_set, predictions)
    
    print(f'Classification Accuracy: {accuracy:.2f}%')

if __name__ == "__main__":
    main()