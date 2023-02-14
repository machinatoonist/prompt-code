# Prompt:
# write a python script to build a multi-class classification 
# machine learning model using xgboost and a sample dataset from 
# sklearn

from sklearn.datasets import load_iris
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

# load data
dataset = load_iris()

# split data into X and y
X = dataset.data
Y = dataset.target

# fit model no training data
model = XGBClassifier()
model.fit(X, Y)

# make predictions for test data
y_pred = model.predict(X)

# evaluate predictions
accuracy = accuracy_score(Y, y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))