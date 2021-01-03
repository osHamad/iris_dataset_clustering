from csv import reader
from matplotlib import pyplot as plt
from sklearn.preprocessing import minmax_scale

def visualize():
    with open('iris.csv', newline='') as iris_data:
        iris_data = list(reader(iris_data))

    attributes = {0:'sepal length (cm)', 1:'sepal width (cm)', 2:'petal length (cm)', 3:'petal width (cm)', 4:'class'}

    for m in range(4):
        for n in range(4):
            if m != n:
                x = [i[m] for i in iris_data]
                y = [i[n] for i in iris_data]

                plt.xlabel(attributes[m])
                plt.ylabel(attributes[n])
                
                x = minmax_scale(x)
                y = minmax_scale(y)

                plt.scatter(x, y)
                plt.show()

if __name__ == '__main__':
    visualize()
