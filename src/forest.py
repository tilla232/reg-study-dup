import numpy as np
import pandas as pd
import clean_data as cd
from sklearn.model_selection import train_test_split

def makeModel(X_train,y_train):
    oob=False
    model = RandomForestClassifier()
    model.fit(X_train,y_train)
    return model



if __name__ == '__main__':
    df = pd.read_csv('../data/Train.csv')
    cd.mister_clean(df)
    WL,SSL,TEX,BL,TTT,MG = cd.split_groups(df)
    cd.delete_empty_columns([WL, SSL, TEX, BL, TTT, MG])
    y = WL['SalePrice'].values
    WL.drop('SalePrice', axis = 1)
    X = WL
    X_train,X_test,y_train, y_test = train_test_split(X,y)
    WLM = makeModel(X_train,y_train)
