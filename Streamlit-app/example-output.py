# Prompt: 
# generate a python script to perform multi-class classification
# using a sample dataset from sklearn

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

# load the iris dataset
dataset = load_iris()

# fit a random forest classifier to the data
model = RandomForestClassifier()
model.fit(dataset.data, dataset.target)

# make predictions
expected_y  = dataset.target
predicted_y = model.predict(dataset.data)

# summarize the fit of the model
print(metrics.classification_report(expected_y, predicted_y))
print(metrics.confusion_matrix(expected_y, predicted_y))