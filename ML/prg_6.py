# Write a program to construct a Bayesian network considering medical data. 
# Use this model to demonstrate the diagnosis of heart patients using standard Heart Disease Data Set.
# You can use Python ML library classes/API.

import pandas as pd
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator

heartDisease = pd.read_csv('heart.csv')
model = BayesianNetwork([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('sex', 'trestbps'), ('exang', 'trestbps'),('trestbps','target'),('fbs','target'),('target', 'restecg'),('target','thalach'),('target','chol')])

model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)

HeartDisease_infer = VariableElimination(model) # Doing exact inference using Variable Elimination

# Query the model
q = HeartDisease_infer.query(variables=['target'], evidence={'age': 34})
print(q)

q = HeartDisease_infer.query(variables=['target'], evidence={'chol': 203}) 
print(q)