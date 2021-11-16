#part 1
import pandas as pd
import matplotlib.pyplot as plt
from_ejudge = pd.read_html("results_ejudge.html")[0]
from_excel = pd.read_excel("students_info.xlsx")
data = pd.merge(from_excel, from_ejudge, how="left", right_on="User", left_on="login")
faculty_average = [data[data["group_faculty"] == i]['Solved'].mean() for i in data["group_faculty"].unique()]
out_average = [data[data["group_out"] == i]['Solved'].mean() for i in data["group_out"].unique()]

plt.title("Average of faculty groups")
plt.bar([i for i in data["group_faculty"].unique()], faculty_average,
        width=0.3, color=['yellow', 'purple', 'black', 'red', 'blue', 'green', 'orange'], alpha=0.9)
plt.show()
plt.clf()

plt.title("Average of out groups")
plt.bar([i for i in data["group_out"].unique()], out_average,
        width=0.3, color=['yellow', 'purple', 'black', 'red', 'blue', 'green', 'orange'], alpha=0.9)
plt.show()

#part 2
print("Transitions in groups")
for gr_fac in data["group_faculty"][(data["G"] > 10) | (data['H'] > 10)]:
    print(gr_fac, end="  ")
print(" ")
for i in range(len(data["group_faculty"][(data["G"] > 10) | (data['H'] > 10)])):
    print("↓", end="  ")
print(" ")
for gr_out in data["group_out"][(data["G"] > 10) | (data['H'] > 10)]:
    print(gr_out, end=" ")
