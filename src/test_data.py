import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import clean_data as cd
import forest as f
import lin_reg as lr
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    df = pd.read_csv('../data/Train.csv')
    cd.mister_clean(df)
    cd.make_dummies(df['Ride_Control'])
    cd.make_dummies(df['Forks'])

    WL, SSL, TEX, BL, TTT, MG = cd.split_groups(df)

    WL_X, WL_y = lr.make_X_y(WL)
    SSL_X, SSL_y = lr.make_X_y(SSL)

    X_train, X_test, y_train, y_test = lr.make_test_split(WL_X, WL_y)
    model = LinearRegression().fit(X_train, y_train)
    print(model.summary)
