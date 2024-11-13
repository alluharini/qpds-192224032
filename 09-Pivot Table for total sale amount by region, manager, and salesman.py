import pandas as pd
data = {'OrderDate': ['1-6-18', '1-23-18', '2-9-18', '2-26-18', '3-15-18', '4-1-18', '4-18-18', '5-5-18', '5-22-18', '6-8-18', 
                      '6-25-18', '7-12-18', '7-29-18', '8-15-18', '9-1-18', '9-18-18'],
        'Region': ['East', 'Central', 'Central', 'Central', 'West', 'East', 'Central', 'Central', 'West', 'East', 
                   'Central', 'East', 'East', 'East', 'Central', 'East'],
        'Manager': ['Martha', 'Hermann', 'Hermann', 'Timothy', 'Timothy', 'Martha', 'Martha', 'Hermann', 'Douglas', 'Martha', 
                    'Hermann', 'Douglas', 'Douglas', 'Martha', 'Douglas','martha'],
        'SalesMan': ['Alexander', 'Shelli', 'Luis', 'David', 'Stephen', 'Alexander', 'Steven', 'Luis', 'Michael', 'Alexander', 
                     'Luis', 'Sigal', 'Karen', 'Alexander', 'John', 'Alexander'],
        'Item': ['Television', 'Home Theater', 'Television', 'Cell Phone', 'Television', 'Home Theater', 'Television', 'Television', 
                 'Television', 'Home Theater', 'Television', 'Television', 'Home Theater', 'Home Theater', 'Desk', 'Video Games'],
        'Units': [95, 50, 36, 27, 56, 60, 75, 90, 32, 60, 90, 29, 81, 35, 2, 16],
        'Unit_price': [1198, 500, 1198, 225, 1198, 500, 1198, 1198, 1198, 500, 1198, 1198, 500, 500, 125, 58.5],
        'Sale_amt': [113810, 25000, 43128, 6075, 67088, 30000, 89850, 107820, 38336, 30000, 107820, 14500, 40500, 41930, 250, 936]}
df = pd.DataFrame(data)
# Create Pivot Table for total sale amount by region, manager, and salesman
pivot_table = pd.pivot_table(df, values='Sale_amt', index=['Region', 'Manager', 'SalesMan'], aggfunc='sum')
print(pivot_table)
