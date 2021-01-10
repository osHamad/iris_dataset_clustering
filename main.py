from sklearn.cluster import KMeans
from csv import reader
from matplotlib import pyplot as plt
from sklearn.preprocessing import minmax_scale

def main():
    with open('iris.csv', newline='') as iris_data:
        iris_data = list(reader(iris_data))

    # we will only be using petal length and width as parameters
    x = [i[2] for i in iris_data]
    y = [i[3] for i in iris_data]
    data = tuple(zip(x, y))


    # we must scale our data before creating the model
    minmax_scale(x)
    minmax_scale(y)

    # training model and making predictions
    model = KMeans(n_clusters=3, max_iter=1000)
    model.fit(data)
    predicted = model.predict(data)

    # plotting the results

if __name__ == '__main__':
    main()
