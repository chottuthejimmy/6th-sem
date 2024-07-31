# Write a program to construct a Bayesian network considering medical data. 
# Use this model to demonstrate the diagnosis of heart patients using standard Heart Disease Data Set. 
# You can use Python ML library classes/API.

import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv("heart.csv")

print('Sample instances from the dataset are given below')
print(heartDisease.head())

model = BayesianNetwork([('age', 'target'), ('sex', 'target'), ('cp', 'target'), ('exang', 'target'), ('target', 'chol'), ('target', 'restecg')])

model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)

HeartDiseasetest_infer = VariableElimination(model)

print('\n1. Probability of HeartDisease given evidence = age')
q1 = HeartDiseasetest_infer.query(variables=['target'], evidence={'age': 37})
print(q1)

print('\n2. Probability of HeartDisease given evidence = chol')
q2 = HeartDiseasetest_infer.query(variables=['target'], evidence={'chol': 233})
print(q2)