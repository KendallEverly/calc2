"""Load CVS file using pandas"""
import pandas as pd
data = pd.read_csv (r'C:\Users\kenda\PycharmProjects\calc2\datafile\data.csv')
"""print the datafile"""
print (data)
"""label values"""
value_a = data.at[0, 'a']
value_b = data.at[0, 'b']
"""operations"""
sum_column = data["a"] + data["b"]
data["Addition"] = sum_column
"""print result"""
print(data)