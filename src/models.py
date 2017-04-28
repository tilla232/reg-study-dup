import clean_data as cd
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


y = cd.WL['SalePrice'].values
cd.WL.drop('SalePrice', axis = 1)
X = cd.WL
print(X.head())
print(X)
print(y)

def makeModel(X_train,y_train):
    oob=False
    model = LinearRegression()
    model.fit(X_train,y_train)
    return model


X_train,X_test,y_train, y_test = train_test_split(X,y)
WLM = makeModel(X_train,y_train)
