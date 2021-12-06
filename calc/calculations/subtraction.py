"""imports"""
import pandas as pd
from datetime import datetime
"""reading"""
filepath = 'C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\data.csv'
data = pd.read_csv(filepath)
results = pd.read_csv('C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\results.csv')
"""Loop for running calc on each input row"""
nrow = data.shape[0]
res_df = pd.DataFrame(columns=['timestamp', 'input filename', 'row num', 'operation', 'result'])
for x in range(0, nrow):
    print("Iter: ", x+1)
    """extract values"""
    value_a = data.at[x, 'a']
    value_b = data.at[x, 'b']
    """operations"""
    calc_result = value_a - value_b
    """initialize list of values"""
    tmpstp = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    res_data = [[tmpstp, filepath, x+1, "Subtraction", calc_result]]
    """Create the pandas DataFrame"""
    res_iter = pd.DataFrame(res_data, columns=['timestamp', 'input filename', 'row num', 'operation', 'result'])
    """Append to results"""
    res_df = res_df.append(res_iter)[['timestamp', 'input filename', 'row num', 'operation', 'result']]
"""Append results to results.csv"""
res_out=results.append(res_df)[['timestamp', 'input filename', 'row num', 'operation', 'result']]
res_out.to_csv('C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\results.csv', index=False)
