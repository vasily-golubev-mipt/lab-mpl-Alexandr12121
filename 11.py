import matplotlib.pyplot as plt
filename = open("001.dat", 'r')
arr = filename.readlines()
k = int(arr[0])

points = arr[1:k+1]
#print(points)
X = []
Y = []

for i in points:
    x, y = (float(item) for item in i.split())

    X.append(x)
    Y.append(y)

plt.plot(X, Y, 'bo')
plt.title('Number of points:  ' + str(k))

plt.show()