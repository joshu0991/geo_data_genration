from common import load_file_kmeans
import matplotlib.pyplot as plt
import math
import time

#%matplotlib inline

import numpy as np
from sklearn.cluster import KMeans
import operator

class KMeanWrapper:
    def __init__(self, file_name, n_clusters, tolerence):
        # X is long lat, and Y are ids/names
        self._X, self._Y = load_file_clus(file_name)
        self._clusters = n_clusters

        """
        # Test small data set
        self._X = np.array([[5, 3, 12],
                      [10, 15, 34],
                      [5, 5, 14],
                      [15, 12, 35],
                      [24, 10, 67],
                      [30, 45, 77],
                      [5, 4, 12],
                      [85, 70, 34],
                      [71, 80, 67],
                      [4, 3, 8],
                      [60, 78, 23],
                      [55, 52, 45],
                      [4, 5, 14],
                      [80, 91, 44], ])
        """

        # start with a small number of clusters adjust later if we need to
        self._kmeans = KMeans(n_clusters=self._clusters)
        self._kmeans.fit(self._X)
        self._tolerence = tolerence

    def get_data_and_labels(self):
        return self._X, self._Y

    def get_centers(self):
        return self._kmeans.cluster_centers_

    def recluster(self, clusters):
        self._clusters = clusters
        self._kmeans = KMeans(n_clusters=clusters)
        self._kmeans.fit(self._X)

    def data_labels(self):
        return self._kmeans.labels_

    def predict(self, arr):
        return self._kmeans.predict(arr)

    def find_cluster(self, label):
        counter = 0
        keys = list()
        cluster = list()

        # Extract all the indecies for the group
        for i in self._kmeans.labels_:
            if i == label:
                keys.append(counter)
            counter = counter + 1

        #print('Keys are ' + str(keys))
        for i in keys:
            cluster.append((self._Y[i], self._X[i], i))

        return cluster

    def find_closest_n(self, size, clus, long, lat, time):
        temp = list()
        ret = list()

        index = 0
        target_euclidean = math.sqrt((long * long) + (lat * lat))
        for i in clus:
            # euclidean of long. and lat.
            euclidean_distance = math.sqrt((float(i[1][0]) * float(i[1][0])) + (float(i[1][1]) * float(i[1][1])))

            magnitude = abs(target_euclidean - euclidean_distance)
            time_delta = abs(time - int(i[1][2]))
            temp.append((magnitude, time_delta, index))
            index = index + 1

        temp = sorted(temp, key=operator.itemgetter(0, 1))
        #print('sorted list is ' + str(temp))

        for i in range(size):
            ret.append(clus[temp[i][2]])
        return ret

    def find_closest_n_resize(self, size, clus, X_prime, long, lat, data_time, label, epsilon, elapsed_time_tolerence):
        clus_size = self._clusters
        ep = 0
        timer_start = time.time()
        best_cluster_size = len(clus)
        best_cluster_number = self._clusters
        time_for_this_clustering = 0

        while len(clus) > self._tolerence and \
                ep < epsilon and \
                time.time() - timer_start < elapsed_time_tolerence:
            cluster_start = time.time()
            print('Total elements in cluster ' + str(len(clus)))
            print('elapsed time ' + str(time.time() - timer_start))
            clus_size = clus_size * 2
            self.recluster(clus_size)
            label =  self._kmeans.predict(X_prime)
            print('New predicted labl ' + str(label))
            clus = self.find_cluster(label)


            if len(clus) < best_cluster_size:
                best_cluster_size = len(clus)
                best_cluster_number = clus_size

            if (time.time() - cluster_start) + (time.time() - timer_start) > elapsed_time_tolerence:
                break

            ep = ep + 1

        if self._clusters != best_cluster_number:
            print('Reverting to a better cluster assignment')
            self.recluster(clus_size)
            clus = self.find_cluster(label)

        print('Total clusters after resizing ' + str(self._clusters))
        return self.find_closest_n(size, clus, long, lat, data_time)

def main():
    print('Starting')

    #km = KMeanWrapper('recent_geo_location_dataset.dat', 4, 5)
    km = KMeanWrapper('recent_geo_location_dataset_small.dat', 4, 5)

    """
        Test data the test data set
    """
    X, Y = km.get_data_and_labels()
    print('labels are ' + str(km.data_labels()))

    # Example long, lat
    #ar = [5, 6]
    ar = [30.659207, -120.79248, 1546107187]
    d = list()
    d.append(ar)
    X_prime = np.array(d)

    predicted_cluster_label = km.predict(X_prime)
    print('predicted label for point is: ' + str(predicted_cluster_label[0]))

    cluster = km.find_cluster(predicted_cluster_label)
    closest_n = km.find_closest_n(2, cluster, ar[0], ar[1], ar[2])
    print('Closest n is ' + str(closest_n))

    closest_n = km.find_closest_n_resize(2, cluster, X_prime, ar[0], ar[1], ar[2], predicted_cluster_label, 10, 1500)
    print('Closest n resize is ' + str(closest_n))

    plt.scatter(X[:,0],X[:,1], label='True Position')
    plt.scatter(X[:,0], X[:,1], c=km.data_labels(), cmap='rainbow')
    plt.scatter(km.get_centers()[:,0] ,km.get_centers()[:,1], color='black')

    print('Done')

if __name__ == "__main__": main()