from common import load_file_kmeans
import matplotlib.pyplot as plt
import math
#%matplotlib inline

import numpy as np
from sklearn.cluster import KMeans

class KMeanWrapper:
    def __init__(self, file_name, n_clusters):
        # X is long lat, and Y are ids/names
        self._X, self._Y = load_file_kmeans(file_name)
        self._clusters = n_clusters

        # Test small data set
        self._X = np.array([[5, 3],
                      [10, 15],
                      [5, 5],
                      [15, 12],
                      [24, 10],
                      [30, 45],
                      [5, 4],
                      [85, 70],
                      [71, 80],
                      [4, 3],
                      [60, 78],
                      [55, 52],
                      [4, 5],
                      [80, 91], ])

        # start with a small number of clusters adjust later if we need to
        self._kmeans = KMeans(n_clusters=self._clusters)
        self._kmeans.fit(self._X)

    def get_data_and_labels(self):
        return self._X, self._Y

    def get_centers(self):
        return self._kmeans.cluster_centers_

    def recluster(self, clusters):
        self._clusters = clusters
        self._kmeans = KMeans(n_clusters=clusters)

    def kmeans_labels(self):
        return self._kmeans.labels_

    def predict(self, arr):
        return self._kmeans.predict(arr)

    def find_cluster(self, label):
        counter = 0
        keys = list()
        cluster = list()
        ret = list()

        # Extract all the indecies for the group
        for i in self.kmeans_labels():
            if i == label:
                keys.append(counter)
            counter = counter + 1

        print('Keys are ' + str(keys))
        for i in keys:
            cluster.append((self._Y[i], self._X[i], i))

        return cluster

    def find_closest_n(self, size, clus, long, lat):
        temp = list()
        ret = list()

        index = 0
        target_euclidean = math.sqrt((long * long) + (lat * lat))
        for i in clus:
            # euclidean of long. and lat.
            euclidean_distance = math.sqrt((i[1][0] * i[1][0]) + (i[1][1] * i[1][1]))
            magnitude = abs(target_euclidean - euclidean_distance)
            temp.append((magnitude, index))
            index = index + 1

        temp = sorted(temp, key=lambda x: x[0])
        print('sorted list is ' + str(temp))
        for i in range(size):
            ret.append(clus[temp[i][1]])

        return ret

print('Starting')

km = KMeanWrapper('recent_geo_location_dataset.dat', 4)

"""
    Test data the test data set
"""
X, Y = km.get_data_and_labels()
print('labels are ' + str(km.kmeans_labels()))

# Example long, lat
ar = [5, 6]
d = list()
d.append(ar)
X_prime = np.array(d)
predicted_cluster_label = km.predict(X_prime)
print('predicted label for [5, 6] is: ' + str(predicted_cluster_label[0]))

cluster = km.find_cluster(predicted_cluster_label)
closest_n = km.find_closest_n(2, cluster, 5, 6)
print('Closest n is ' + str(closest_n))

plt.scatter(X[:,0],X[:,1], label='True Position')
plt.scatter(X[:,0], X[:,1], c=km.kmeans_labels(), cmap='rainbow')
plt.scatter(km.get_centers()[:,0] ,km.get_centers()[:,1], color='black')

print('Done')