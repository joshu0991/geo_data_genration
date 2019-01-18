import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from common import load_file_clus

class AgglomerativeCluster:
    def __init__(self, file_name, cluster_numbers):
        self._X, self._Y = load_file_clus(file_name)
        self._X = self._X.astype(np.float64)
        self._linked = linkage(self._X, 'single')
        self._cluster = AgglomerativeClustering(n_clusters=cluster_numbers, affinity='euclidean', linkage='ward')
        self._cluster.fit_predict(self._X)


    def get_labels(self):
        return self._cluster.labels_

    def plot(self, range_upper):
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

    def plot_2(self):
        plt.scatter(self._X[:, 0], self._X[:, 1], c=self._cluster.labels_, cmap='rainbow')


ag = AgglomerativeCluster('recent_geo_location_dataset_small.dat', 4)
plt.scatter(ag._X[:,0],ag._X[:,1], c=ag.get_labels(), cmap='rainbow')

