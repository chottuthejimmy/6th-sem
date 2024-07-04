# Write a program to implement the naive Bayesian classifier 
# for a sample training data set stored as a .CSV file. 
# Compute the accuracy of the classifier, considering few test data sets.

import csv
import random
import math
from collections import defaultdict

def load_csv(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        dataset = [list(map(float, row)) for row in csv.reader(file)]
    return dataset

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
    for class_value, rows in separated.items():
        summaries[class_value] = [(sum(col) / len(col), math.sqrt(sum((x - sum(col) / len(col)) ** 2 for x in col) / (len(col) - 1))) 
                                  for col in zip(*rows)]
    return summaries

def calculate_class_probabilities(summaries, row):
    probabilities = {}
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = 1
        for i, (mean, stdev) in enumerate(class_summaries):
            x = row[i]
            probabilities[class_value] *= (1 / (math.sqrt(2 * math.pi) * stdev)) * math.exp(-((x-mean)**2 / (2 * stdev**2)))
    return probabilities

def predict(summaries, row):
    probabilities = calculate_class_probabilities(summaries, row)
    return max(probabilities, key=probabilities.get)

def get_prediction(train, test):
    summaries = summarize_by_class(train)
    predictions = [predict(summaries, row) for row in test]
    return predictions

def accuracy(test_set, predictions):
    correct = sum(test_row[-1] == pred for test_row, pred in zip(test_set, predictions))
    return (correct / len(test_set)) * 100.0

def main():
    filename = 'diabetes.csv'
    dataset = load_csv(filename)
    train_set, test_set = train_test_split(dataset, 0.87)
    print(f'Dataset split: training={len(train_set)}, testing={len(test_set)}')
    predictions = get_prediction(train_set, test_set)
    accuracy_score = accuracy(test_set, predictions)
    print(f'Classification Accuracy: {accuracy_score:.2f}%')

if __name__ == "__main__":
    main()