import numpy as np
import pandas as pd
from src import clean_data

df = pd.read_csv('data/Train.csv')
df1 = df.loc[:, 'fiModelDescriptor': 'Transmission']
df1.drop('ProductGroup', inplace=True, axis=1)
df1.rename(columns={'ProductGroupDesc':'ProductGroup'})

WL, SSL, TEX, BL, TTT, MG = clean_data.make_product_df(df)


def n_uniques(lst, names):
    for i, product in enumerate(lst):
        print('\n{0}: '.format(names[i]))
        for col in product.columns:
            print('{0}: '.format(col), product[col].nunique())

def delete_empty_columns(lst):
    for product in lst:
        for col in product.columns:
            if product[col].nunique() == 0:
                product.drop(col, inplace=True, axis=1)
            elif product[col].nunique() == 1:
                product.drop(col, inplace=True, axis=1)

def make_temp_dfs(lst1, lst2):
    for product in lst1:
        temp = product.loc[:, 'fiModelDescriptor':'Enclosure']

def replace_null(df):
    df.replace('None or Unspecified', np.nan)
if __name__ == '__main__':
    product_lst = [WL, SSL, TEX, BL, TTT, MG]
    product_name = ['WL', 'SSL', 'TEX', 'BL', 'TTT', 'MG']
    # n_uniques(product_lst, product_name)
    delete_empty_columns(product_lst)
