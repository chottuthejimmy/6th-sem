# Write a program to implement k-Nearest Neighbour algorithm to classify the iris data set.
# Print both correct and wrong predictions.
# Java/Python ML library classes can be used for this problem.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier

iris=load_iris()
X=iris.data
y=iris.target

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

for i in range(len(iris.target_names)):
    print("Label", i , "-",str(iris.target_names[i]))

clf = KNeighborsClassifier(n_neighbors=2)
clf.fit(x_train, y_train)

y_pred=clf.predict(x_test)
print("Results of Classification using K-nn with K = 2 ")

for i in range(len(x_test)):
    print("Sample:", str(x_test[i]), " Actual-label:", str(y_test[i])," Predicted-label:", str(y_pred[i]))
    print("\n")

print("Classification Accuracy :" , clf.score(x_test,y_test))