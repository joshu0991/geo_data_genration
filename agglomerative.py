import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from common import load_file_clus

import matplotlib.pyplot as plt
# Though the following import is not directly being used, it is required
# for 3D projection to work
from mpl_toolkits.mplot3d import Axes3D


class AgglomerativeCluster:
    def __init__(self, file_name, cluster_numbers):
        self._X, self._Y = load_file_clus(file_name)
        """
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
        self._X = self._X.astype(np.float64)
        self._cluster = AgglomerativeClustering(n_clusters=cluster_numbers, affinity='euclidean', linkage='ward')
        self._cluster.fit_predict(self._X)


    def get_labels(self):
        return self._cluster.labels_

    def plot_points_3d(self):
        fignum = 1
        fig = plt.figure(fignum, figsize=(4, 3))
        ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
        labels = self.get_labels()

        ax.scatter(self._X[:, 0], self._X[:, 1], self._X[:, 2],
                   c=labels.astype(np.float), edgecolor='k')

        ax.w_xaxis.set_ticklabels([])
        ax.w_yaxis.set_ticklabels([])
        ax.w_zaxis.set_ticklabels([])
        ax.set_xlabel('longitude')
        ax.set_ylabel('latitude')
        ax.set_zlabel('time')
        ax.dist = 12
        plt.show()

    def plot_dendogram(self):
        linked = linkage(self._X, 'single')

        labelList = self.get_labels()

        plt.figure(figsize=(10, 7))
        dendrogram(linked,
                   orientation='top',
                   labels=labelList,
                   distance_sort='descending',
                   show_leaf_counts=True)
        plt.show()


ag = AgglomerativeCluster('recent_geo_location_dataset_small.dat', 6)
#ag.plot_points_3d()
ag.plot_dendogram()