import pandas as pd

# df = pd.read_csv('../data/Train.csv')
# print(df.columns)
# _______________ COLUMN NAMES _______________________
#'SalesID', 'SalePrice', 'MachineID', 'ModelID', 'datasource',
#        'auctioneerID', 'YearMade', 'MachineHoursCurrentMeter', 'UsageBand',
#        'saledate', 'fiModelDesc', 'fiBaseModel', 'fiSecondaryDesc',
#        'fiModelSeries', 'fiModelDescriptor', 'ProductSize',
#        'fiProductClassDesc', 'state', 'ProductGroup', 'ProductGroupDesc',
#        'Drive_System', 'Enclosure', 'Forks', 'Pad_Type', 'Ride_Control',
#        'Stick', 'Transmission', 'Turbocharged', 'Blade_Extension',
#        'Blade_Width', 'Enclosure_Type', 'Engine_Horsepower', 'Hydraulics',
#        'Pushblock', 'Ripper', 'Scarifier', 'Tip_Control', 'Tire_Size',
#        'Coupler', 'Coupler_System', 'Grouser_Tracks', 'Hydraulics_Flow',
#        'Track_Type', 'Undercarriage_Pad_Width', 'Stick_Length', 'Thumb',
#        'Pattern_Changer', 'Grouser_Type', 'Backhoe_Mounting', 'Blade_Type',
#        'Travel_Controls', 'Differential_Type', 'Steering_Controls'],
#       dtype='object'

### superfluous object column
df.drop('fiModelDesc',axis=1,inplace=True)
df.drop('Backhoe_Mounting',axis=1,inplace=True)

### clean string values
df['fiSecondaryDesc'] = df['fiSecondaryDesc'].apply(lambda x: None if x == '#NAME?' else x)
df['fiSecondaryDesc'] = df['fiSecondaryDesc'].apply(lambda x: 'B' if x == 'B     ' else x)
df['fiSecondaryDesc'] = df['fiSecondaryDesc'].apply(lambda x: 'M' if x == 'M      ' else x)
df['fiSecondaryDesc'] = df['fiSecondaryDesc'].apply(lambda x: 'C' if x == 'C      ' else x)
df['fiSecondaryDesc'] = df['fiSecondaryDesc'].apply(lambda x: 'H' if x == 'H      ' else x)
df['fiSecondaryDesc'] = df['fiSecondaryDesc'].apply(lambda x: 'MSR SPIN ACE' if x == ' MSR SPIN ACE' else x)
df['fiModelSeries'] = df['fiModelSeries'].apply(lambda x: None if x == '#NAME?' else x)
df['fiModelSeries'] = df['fiModelSeries'].apply(lambda x: 'II' if x == 'SeriesII' else x)
df['fiModelSeries'] = df['fiModelSeries'].apply(lambda x: '7' if x == '7.00E+00' else x)
df['fiModelSeries'] = df['fiModelSeries'].apply(lambda x: '6' if x == '6.00E+00' else x)
df['fiModelSeries'] = df['fiModelSeries'].apply(lambda x: '-15' if x == '-1.50E+01' else x)
df['fiModelSeries'] = df['fiModelSeries'].str.replace('.0','')

### these will be for if we want to subset our data with the non-nulls;
### if the prediction rate for the non-nulls isn't affected,
### we can just outright drop the column

df_neers = df[df['auctioneerID'].notnull()]
df_meter = df[df['MachineHoursCurrentMeter'].notnull()]
df_band = df[df['UsageBand'].notnull()]
df_series = df[df['fiModelSeries'].notnull()]

#____________ PRODUCT GROUPS _______________________
#['WL' 'SSL' 'TEX' 'BL' 'TTT' 'MG']

WL = df[df['ProductGroup'] == 'WL']
SSL = df[df['ProductGroup'] == 'SSL']
TEX = df[df['ProductGroup'] == 'TEX']
BL = df[df['ProductGroup'] == 'BL']
TTT = df[df['ProductGroup'] == 'TTT']
MG = df[df['ProductGroup'] == 'MG']


def n_uniques(lst, names):
    '''
    lst = [WL, SSL, TEX, BL, TTT, MG]
    names = ['WL', 'SSL', 'TEX', 'BL', 'TTT', 'MG']
    '''
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

def replace_null(df):
    df.replace('None or Unspecified', np.nan, inplace=True)
