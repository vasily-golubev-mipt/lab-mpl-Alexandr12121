import matplotlib.pyplot as plt
filenames = ["001.dat", "002.dat", "003.dat", "004.dat", "005.dat"]
for filename in filenames:
    name = open(filename, 'r')
    arr = name.readlines()
    k = int(arr[0])
    points = arr[1:k+1]
    X = []
    Y = []
    for point in points:
        x, y = (float(coord) for coord in point.split())
        X.append(x)
        Y.append(y)
    plt.plot(X, Y, 'bo')
    plt.title('Number of points:  ' + str(k))
    plt.show()
