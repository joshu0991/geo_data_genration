import numpy as np
from csv import reader

def load_file(file_name):
    data = list()
    labels = list()
    with open(file_name, 'r') as file:
        csv_reader = reader(file)
        for r in csv_reader:
            if not r:
                continue
            label = r[0]
            del r[0]
            data.append(r)
            labels.append(label)

    X = np.array(data)
    Y = np.array(labels)
    return X, Y

def load_file_kmeans(file_name):
    data = list()
    labels = list()
    with open(file_name, 'r') as file:
        csv_reader = reader(file)
        for r in csv_reader:
            if not r:
                continue
            id = r[0]
            long = r[1]
            lat = r[2]
            arr = [long, lat]
            data.append(arr)
            labels.append(id)

    X = np.array(data)
    Y = np.array(labels)
    return X, Y