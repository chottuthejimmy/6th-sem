# For the given dataset mtcars.csv (www.kaggle.com/ruiromanini/mtcars), 
# plot a histogram to check the frequency distribution of the variable ‘mpg’ (Miles per gallon)

import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')
plt.hist(mtcars['mpg'], edgecolor='black')

plt.xlabel('Miles per gallon (mpg)')
plt.ylabel('Frequency')
plt.title('Histogram of Miles per gallon (mpg)')
plt.show()