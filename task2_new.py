import matplotlib.pyplot as plt
file_name = open("file1.txt", 'r')
arr = file_name.readlines()
print("Amount of frames:  " + str(len(arr)))
number_of_frame = 0
for even in range(0, 11, 2):
        x = arr[even].split()
        y = arr[even + 1].split()
        for j in range(len(x)):
            x[j], y[j] = map(float, (x[j], y[j]))
        fig, axes = plt.subplots()
        axes.plot(x, y, marker='', linestyle='--', color='green', linewidth=2)
        plt.ylim([-15, 15])
        plt.xlim([min(x), max(x)])
        axes.set_title("Frame: " + str(number_of_frame))
        axes.grid()
        plt.show()
        number_of_frame += 1
