import pandas as pd

df = pd.read_csv('../data/Train.csv')
print(df.columns)
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


#____________ PRODUCT GROUPS _______________________
#['WL' 'SSL' 'TEX' 'BL' 'TTT' 'MG']
WL = df[df['ProductGroup'] == 'WL']
SSL = df[df['ProductGroup'] == 'SSL']
TEX = df[df['ProductGroup'] == 'TEX']
BL = df[df['ProductGroup'] == 'BL']
TTT = df[df['ProductGroup'] == 'TTT']
MG = df[df['ProductGroup'] == 'MG']


# total = WL.shape[0]+ SSL.shape[0] + TEX.shape[0] + BL.shape[0]+ TTT.shape[0] + MG.shape[0]
# print(total)
