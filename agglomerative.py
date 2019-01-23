import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from common import load_file_clus
from mpl_toolkits.mplot3d import Axes3D

class AgglomerativeCluster:
    def __init__(self, file_name, cluster_numbers):
        self._X, self._Y = load_file_clus(file_name)

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

        self._X = self._X.astype(np.float64)
        self._cluster = AgglomerativeClustering(n_clusters=cluster_numbers, affinity='euclidean', linkage='ward')
        self._cluster.fit_predict(self._X)


    def get_labels(self):
        return self._cluster.labels_

    def plot_points_2d(self, range_upper):
        labels = range(1, range_upper)
        plt.figure(figsize=(10, 7))
        plt.subplots_adjust(bottom=0.1)
        plt.scatter(X[:, 0], X[:, 1], label='True Position')

        for label, x, y in zip(labels, X[:, 0], X[:, 1]):
            plt.annotate(
                label,
                xy=(x, y), xytext=(-3, 3),
                textcoords='offset points', ha='right', va='bottom')
        plt.show()

    def plot_clusters_2d(self):
        plt.scatter(self._X[:, 0], self._X[:, 1], c=self._cluster.labels_, cmap='rainbow')
        plt.show()

    def plot_points_3d(self):
        pass

    def plot_clusters_3d(self):
        pass

    def plot_dendogram(self):
        pass

"""
ag = AgglomerativeCluster('recent_geo_location_dataset_small.dat', 2)
plt.scatter(ag._X[:,0],ag._X[:,1], c=ag.get_labels(), cmap='rainbow')
plt.show()
"""
