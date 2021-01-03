from sklearn.cluster import KMeans
from csv import reader
from matplotlib import pyplot as plt

def main():
    with open('iris.csv', newline='') as iris_data:
        iris_data = list(reader(iris_data))

    set_data = [[i[2], i[3]] for i in iris_data]

    km = KMeans(n_clusters=3)
    predicted = km.fit_predict(set_data)
    print(predicted)

if __name__ == '__main__':
    main()
