import pandas as pd
import matplotlib.pyplot as plt
file_read = pd.read_csv("flights.csv")
flights = file_read.CARGO.value_counts()
prices = file_read.groupby("CARGO").PRICE.sum()
weights = file_read.groupby("CARGO").WEIGHT.sum()

data_set = pd.DataFrame({'CARGO': flights, 'PRICE': prices, 'WEIGHT': weights})
print(data_set)
data_set.plot(kind="pie", subplots=True, figsize=(15,4))
plt.show()
