import numpy as np
import pandas as pd
import clean_data as cd
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    df = pd.read_csv('../data/Train.csv')
    cd.mister_clean(df)
    WL,SSL,TEX,BL,TTT,MG = cd.split_groups(df)
    cd.delete_empty_columns([WL, SSL, TEX, BL, TTT, MG])

    
