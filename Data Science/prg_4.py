# Train a regularized logistic regression classifier on the iris dataset (https://archive.ics.uci.edu/ml/machine-learning-databases/iris/ or the inbuilt iris dataset) using sklearn. 
# Train the model with the following hyperparameter C = 1e4 and report the best classification accuracy.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = make_pipeline(StandardScaler(), LogisticRegression(C=1e4, max_iter=1000))

pipeline.fit(X_train, y_train)

accuracy = pipeline.score(X_test, y_test)
print("Classification accuracy:", accuracy)