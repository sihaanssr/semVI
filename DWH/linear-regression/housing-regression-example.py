import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
dataset = pd.read_csv('housing.csv')

X = pd.DataFrame(dataset.iloc[:,:-1])
Y = pd.DataFrame(dataset.iloc[:,-1])
X_train,X_test,Y_train,Y_test = train_test_split(test_size=0.2,random_state=0.5)
regressor = LinearRegression()
regressor.fit(X_train,Y_train)