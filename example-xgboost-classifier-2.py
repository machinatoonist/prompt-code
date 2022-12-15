# Prompt: write a python script to build a multi-class 
# classification machine learning model using the iris sample dataset from sklearn and xgboost
# Temperature: 0.9
# Notes:
# Initial code suggestion failed because df['species'] was used to fit model and
# required numerical values. This was fixed by using dataset.target instead.

# import necessary libraries
import pandas as pd
from sklearn import datasets
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

# load the iris dataset
dataset = datasets.load_iris()

# build a dataframe from the dataset
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

# add the target variable to the dataframe
df['species'] = pd.Categorical.from_codes(dataset.target, dataset.target_names)

# create a list of feature columns
features = df.columns.drop('species')

# create the xgboost classifier
xgb = XGBClassifier()

df['species']

df[features]

# train the classifier
xgb.fit(df[features], dataset.target)

# make predictions
predictions = xgb.predict(df[features])

# print the accuracy
print(f'Accuracy: {accuracy_score(dataset.target, predictions)*100:.1f}%')