from sklearn.cluster import KMeans
from csv import reader

def main():
    with open('iris.csv', newline='') as iris_data:
        iris_data = list(reader(iris_data))

    print(iris_data)

if __name__ == '__main__':
    main()
