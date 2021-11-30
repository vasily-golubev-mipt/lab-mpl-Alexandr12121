import csv
import matplotlib.pyplot as plt
import matplotlib.colors
try:
    with open("students.csv") as fp:
        data = csv.reader(fp, delimiter=";", quotechar='"')
        new_data = [row for row in data]
except:
    pass

prep_names = ["prep1", "prep2", "prep3", "prep4", "prep5", "prep6", "prep7"]
group_names = ["751", "752", "753", "754", "755", "756"]
color_names = ['red', 'yellow',  'palevioletred', 'green', 'gray', 'magenta', 'orange','mediumspringgreen', 'red', 'blue']
mark_names = ["3", "4", "5", "6", "7", "8", "9", "10"]
def plt_it(name, n):
    marks = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(new_data)):
        if new_data[i][n] == name:
            for j in range(3, 11, 1):
                if new_data[i][2] == str(j):
                    marks[j - 2] += 1
    count = 0
    for i in range(3, 11, 1):
        plt.bar(name, marks[i - 2], bottom=marks[i - 3]+count, color=color_names[::-1][i - 3],
                label=mark_names[i - 3])
        count += marks[i - 3]


fig1 = plt.figure()
plt.title("marks -- prep")
for prep_name in prep_names:
    plt_it(prep_name, 0)
plt.legend(["3", "4", "5", "6", "7", "8", "9", "10"])
plt.show()
 
fig2 = plt.figure()
plt.title("marks -- group")
for group_name in group_names:
    plt_it(group_name, 1)
plt.legend(["3", "4", "5", "6", "7", "8", "9", "10"])
plt.show()
