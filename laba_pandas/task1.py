import pandas as pd
arr_for_Umbrella = []
arr = pd.read_csv("transactions.csv")
Real = arr[arr['STATUS'] == 'OK']
print("Three biggest: \n", Real.loc[Real['SUM'].nlargest(3).index])
print("Summa of Umbrella transactions: \n", Real.loc[Real['CONTRACTOR'] == 'Umbrella, Inc']['SUM'].sum())
