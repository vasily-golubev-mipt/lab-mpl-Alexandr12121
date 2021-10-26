import matplotlib.pyplot as plt

file_name = open("file1.txt", 'r')
arr = file_name.readlines()
#print(arr)

print("Amount of frames:  " + str(len(arr)))
number_of_frame = 0
even = 0

while even < len(arr):

        j = even

        x = arr[j].split()
        y = arr[j + 1].split()
        for j in range(len(x)):

            x[j], y[j] = map(float, (x[j], y[j]))

        fig, axes = plt.subplots()

        axes.plot(x, y, marker='', linestyle='--', color='green', linewidth=2)
        plt.ylim([-15, 15])
        plt.xlim([0, 15])

        axes.set_title("Frame: " + str(number_of_frame))
        number_of_frame = number_of_frame + 1
        axes.grid()
        plt.show()
        even += 2
