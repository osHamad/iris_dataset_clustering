from csv import reader
from matplotlib import pyplot as plt
from sklearn.preprocessing import minmax_scale

def visualize():
    # converting data file into a python list
    with open('iris.csv', newline='') as iris_data:
        iris_data = list(reader(iris_data))

    # dictionary with all attribute names and order
    attributes = {0:'sepal length (cm)', 1:'sepal width (cm)',
     2:'petal length (cm)', 3:'petal width (cm)', 4:'class'}

     # using a for loop to plot all possible combinations of attributes
    for m in range(4):
        for n in range(4):
            if m != n:
                x = [i[m] for i in iris_data]
                y = [i[n] for i in iris_data]

                plt.xlabel(attributes[m])
                plt.ylabel(attributes[n])

                # scaling data to give the best results
                x = minmax_scale(x)
                y = minmax_scale(y)

                # plotting and showing points
                plt.scatter(x, y)
                plt.show()

if __name__ == '__main__':
    visualize()
