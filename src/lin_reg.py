import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import clean_data as cd
import forest as f
from sklearn.model_selection import train_test_split

## import important features from RF
def make_X_y(df):
    y = df['SalePrice'].values
    X = df.drop('SalePrice', axis=1).values
    return X, y

def make_test_split(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    cd.mister_clean(cd.df)
    y = cd.df['SalePrice'].values
    df1 = cd.df.drop('SalePrice', axis=1)
    X = cd.df1.values

    X_train, X_test, y_train, y_test = make_test_split(X, y)
    model = LinearRegression().fit(X_train, y_train)
    model.predict(X_test)
    print(model.summary)
