import numpy as np
import pandas as pd
import clean_data as cd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    df = pd.read_csv('../data/Train.csv')
    X = cd.mister_clean(df)
    df2 = pd.read_csv('../data/Train.csv')
    y = df2[['SalePrice']]
    # cd.make_dummies(df['Ride_Control'])
    # cd.make_dummies(df['Forks'])
    # cd.make_dummies(df['Coupler_System'])
    # cd.make_dummies(df['Grouser_Tracks'])
    # WL,SSL,TEX,BL,TTT,MG = cd.split_groups(X)
    # cd.delete_empty_columns([WL, SSL, TEX, BL, TTT, MG])
    #
    # BL_y = np.array(BL[BL.columns[0]])
    # BL_X = np.array(BL[BL.columns[1:]])
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    rf = RandomForestClassifier()
    rf.fit(X_train,y_train)
