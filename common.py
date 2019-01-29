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

def load_file_clus(file_name):
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
            time = r[5]
            arr = [long, lat, time]
            data.append(arr)
            labels.append(id)

    X = np.array(data)
    Y = np.array(labels)
    return X, Y

def load_file_outliers(file_name):
    data = list()
    with open(file_name, 'r') as file:
        csv_reader = reader(file)
        for r in csv_reader:
            if not r:
                continue
            id = r[0]
            long = r[1]
            lat = r[2]
            time = r[3]
            arr = [long, lat, time]
            data.append(arr)
    X = np.array(data)
    return X

def load_file_outliers_space_time(file_name):
    data_X = list()
    data_Y = list()
    with open(file_name, 'r') as file:
        csv_reader = reader(file)
        for r in csv_reader:
            if not r:
                continue
            id = r[0]
            long = r[1]
            lat = r[2]
            time = r[3]
            arr = [long, lat]
            data_X.append(arr)
            data_Y.append(time)
    X = np.array(data_X)
    Y = np.array(data_Y)
    return X, Y