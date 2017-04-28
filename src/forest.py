import numpy as np
import pandas as pd
import clean_data as cd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    df = pd.read_csv('../data/Train.csv')
    X = cd.mister_clean(df)
    WL,SSL,TEX,BL,TTT,MG = cd.split_groups(X)
    WL_dummies = cd.get_dummies(WL)
    SSL_dummies = cd.get_dummies(SSL)
    TEX_dummies = cd.get_dummies(TEX)
    BL_dummies = cd.get_dummies(BL)
    TTT_dummies = cd.get_dummies(TTT)
    MG_dummies = cd.get_dummies(MG)

    df2 = pd.read_csv('../data/Train.csv')
    y = df2[['SalePrice','ProductGroup']]
    BL_y = np.array(y[y['ProductGroup'] == 'BL'])
    # cd.make_dummies(df['Ride_Control'])
    # cd.make_dummies(df['Forks'])
    # cd.make_dummies(df['Coupler_System'])
    # cd.make_dummies(df['Grouser_Tracks'])
    # cd.delete_empty_columns([WL, SSL, TEX, BL, TTT, MG])
    #
    # BL_y = np.array(BL[BL.columns[0]])
    # BL_X = np.array(BL[BL.columns[1:]])
    X_train, X_test, y_train, y_test = train_test_split(BL_dummies, BL_y)

    rf = RandomForestClassifier()
    rf.fit(X_train,y_train)
