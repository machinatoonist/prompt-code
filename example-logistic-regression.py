# prompt: create a python script to build a 
# logistic regression model for classification 
# using the iris sample dataset from sklearn
# temperature: 0.5

from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# load the iris dataset
dataset = datasets.load_iris()

# fit a logistic regression model to the data
model = LogisticRegression()
model.fit(dataset.data, dataset.target)

# make predictions
expected = dataset.target
predicted = model.predict(dataset.data)

# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))