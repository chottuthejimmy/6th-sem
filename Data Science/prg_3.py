# Consider the books dataset BL-Flickr-Images-Book.csv from Kaggle (https://www.kaggle.com/adeyoyintemidayo/publication-of-books) which contains information about books. 
# Write a program to demonstrate the following.
# Import the data into a DataFrame
# Find and drop the columns which are irrelevant for the book information.
# Change the Index of the DataFrame
# Tidy up fields in the data such as date of publication with the help of simple regular expression.
# Combine str methods with NumPy to clean columns

import pandas as pd
import numpy as np

df = pd.read_csv('BL-Flickr-Images-Book.csv')
print("Original DataFrame:")
print(df.head())

irrelevant_columns = ['Edition Statement', 'Contributors', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Issuance type', 'Shelfmarks']
df.drop(columns=irrelevant_columns, inplace=True)

df.set_index('Identifier', inplace=True)

df['Date of Publication'] = df['Date of Publication'].str.extract(r'^(\d{4})')
df['Place of Publication'] = np.where(df['Place of Publication'].str.contains('London'), 'London', df['Place of Publication'].str.replace('-', ' '))

print("\nCleaned DataFrame:")
print(df.head())