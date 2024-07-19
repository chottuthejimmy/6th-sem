# A study was conducted to understand the effect of number of hours the students spent studying on their performance in the final exams.
# Write a code to plot line chart with number of hours spent studying on x-axis and score in final exam on y-axis.
# Use a red ‘*’ as the point character, label the axes and give the plot a title.

import matplotlib.pyplot as plt

hours = [10,9,2,15,10,16,11,16]
score = [95,80,10,50,45,98,38,93]

plt.plot(hours, score, marker='*', color='red')
plt.xlabel('Number of Hours Studied')
plt.ylabel('Score in Final Exam')
plt.title('Effect of Hours Studied on Exam Score')
plt.grid() # Add grid lines
plt.show()