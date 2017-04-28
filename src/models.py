import clean_data as cd
import pandas as pd
import numpy as np
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error,precision_score, recall_score
from sklearn import preprocessing

def makeTests(df):
    y = df['SalePrice'].values
    WL.drop('SalePrice', axis = 1)
    X = df[['MachineID','ModelID','datasource','auctioneerID','YearMade','MachineHoursCurrentMeter']]

    return train_test_split(X,y)

def makeModel(X_train,y_train):
    oob=False
    model = RandomForestClassifier()
    model.fit(X_train,y_train)
    feats = model.feature_importances_
    # dic = {}
    # for x,feat in enumerate(feats):
    #     dic[x] = feat
    return model

def ManyModels(df):
    X_train,X_test,y_train, y_test = makeTests(df)
    mod = makeModel(X_train,y_train)
    mod.fit(X_train,y_train).score(X_test, y_test)
    return mod

def linearReg(df):
    X_train,X_test,y_train, y_test = makeTests(df)
    mod = LinearRegression()
    mod.fit(X_train,y_train).score(X_test, y_test)
    return mod

if __name__ == '__main__':
    df = pd.read_csv('../data/Train.csv')
    cd.mister_clean(df)
    WL,SSL,TEX,BL,TTT,MG = cd.split_groups(df)
    WL = WL.fillna(value=0)
    cd.delete_empty_columns([WL, SSL, TEX, BL, TTT, MG])
    lst = [WL, SSL, TEX, BL, TTT, MG]

    X_train,X_test,y_train, y_test = makeTests(WL)
    WLM = ManyModels(WL)
    SSLM = ManyModels(WL)
    TEX = ManyModels(TEX)
    BL = ManyModels(BL)
    TTT = ManyModels(TTT)
    MG = ManyModels(MG)

    print(WLM.feature_importances_)
    print(SSLM.feature_importances_)
    print(TEX.feature_importances_)
    print(BL.feature_importances_)
    print(TTT.feature_importances_)
    print(MG.feature_importances_)

    #CHANGE Feature Importane
    # NWL = WLM[]
    # SSL = SSL[]
    # TEX = TEX[]
    # BL = BL[]
    # TTT = TTT[]
    # MG = MG[]
    #
    # WLL = linearReg(nWL)
