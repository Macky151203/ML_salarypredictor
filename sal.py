import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def salprediction(number):

    dataset = pd.read_csv('Salary_Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    NX_test=np.array(number,dtype=float)
    NX_test=NX_test.reshape((1,-1))
    y_pred = regressor.predict(NX_test)
    print(y_pred)
    return y_pred

salprediction(15)


