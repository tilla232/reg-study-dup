import pandas as pd

df = pd.read_csv('../data/Train.csv')
#print(df.columns)
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



#df[['Turbocharged', 'Blade_Extension', 'Blade_Width','Enclosure_Type','Engine_Horsepower','Hydraulics','Pushblock','Ripper', 'Scarifier', 'Tip_Control', 'Tire_Size', 'Coupler', 'Coupler_System']]

print(df.Turbocharged.unique())


# Turbocharged  [nan]
# Blade_Extension  ['Yes' 'None or Unspecified' nan]
# Blade_Width  ['None or Unspecified' "12'" "14'" "13'" "16'" "<12'" nan]
# Enclosure_Type  ['None or Unspecified' 'Low Profile' 'High Profile' nan]
# Engine_Horsepower  ['No' 'Variable' nan]
# Hydraulics  ['Base + 1 Function' 'Base + 3 Function' 'Base + 2 Function'
#  'Base + 4 Function' 'Base + 5 Function' 'Base + 6 Function' 'Standard'
#  '2 Valve' nan 'Auxiliary' '3 Valve']
# Pushblock  ['None or Unspecified' 'Yes' nan]
# Ripper  ['None or Unspecified' 'Yes' nan 'Single Shank' 'Multi Shank']
# Scarifier  [nan 'Yes' 'None or Unspecified']
# Tip_Control  [nan 'Sideshift & Tip' 'None or Unspecified' 'Tip']
# Tire_Size  ['None or Unspecified' '23.5' nan '13"' '26.5' '29.5' '14"' '20.5' '17.5"'
#'15.5"' '20.5"' '17.5' '7.0"' '15.5' '23.5"' '10"' '23.1"' '10 inch']
# Coupler  ['None or Unspecified' nan 'Manual' 'Hydraulic']
# Coupler_System  [nan 'None or Unspecified' 'Yes']


# total = WL.shape[0]+ SSL.shape[0] + TEX.shape[0] + BL.shape[0]+ TTT.shape[0] + MG.shape[0]
# print(total)
