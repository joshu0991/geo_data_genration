import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from common import load_file_outliers
from mpl_toolkits.mplot3d import Axes3D

class IsoForest:
    def __init__(self, file_name, max_samples):
        self._X = load_file_outliers(file_name)
        self._X = self._X.astype(np.float64)
        rng = np.random.RandomState(42)
        self._iso = IsolationForest(behaviour='new', max_samples=max_samples,
                                    random_state=rng, contamination='auto')

    def train(self, data):
        self._iso.fit(data)

    def test_set(self, normal, outliers):
        y_pred_test = self._iso.predict(normal)
        y_pred_outliers = self._iso.predict(outliers)
        return y_pred_test, y_pred_outliers

    def plot_long_lat(self, train, norm, outliers):
        #xx, yy, zz = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
        #Z = self._iso.decision_function(np.c_[xx.ravel(), yy.ravel(), zz.ravel()])
        #Z = Z.reshape(xx.shape)

        #plt.title("IsolationForest")
        #plt.contourf(xx, yy, Z, cmap=plt.cm.Blues_r)

        fignum = 1
        fig = plt.figure(fignum, figsize=(4, 3))
        ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

        ax.scatter(train[:, 0], train[:, 1], train[:, 2],
                   c='white', edgecolor='k')

        ax.scatter(norm[:, 0], norm[:, 1], norm[:, 2],
                   c='green', edgecolor='k')

        ax.scatter(outliers[:, 0], outliers[:, 1], outliers[:, 2],
                   c='red', edgecolor='k')

        ax.w_xaxis.set_ticklabels([])
        ax.w_yaxis.set_ticklabels([])
        ax.w_zaxis.set_ticklabels([])
        ax.set_xlabel('longitude')
        ax.set_ylabel('latitude')
        ax.set_zlabel('time')
        ax.dist = 12
        plt.show()

        """
        b1 = plt.scatter(train[:, 0], train[:, 1], c='white',
                         s=20, edgecolor='k')
        b2 = plt.scatter(norm[:, 0], norm[:, 1], c='green',
                         s=20, edgecolor='k')
        c = plt.scatter(outliers[:, 0], outliers[:, 1], c='red',
                        s=20, edgecolor='k')
        plt.axis('tight')
        plt.xlim((-5, 5))
        plt.ylim((-5, 5))
        plt.legend([b1, b2, c],
                   ["training observations",
                    "new regular observations", "new abnormal observations"],
                   loc="upper left")
        plt.show()
        """

iso = IsoForest('pol_recent_geo_location_dataset_small.dat', 12)

length = len(iso._X)
train_length = int(length/2)
outlier_start = length - 4

outliers = iso._X[outlier_start:]
train = iso._X[0:train_length]
test_train = iso._X[train_length:outlier_start]

iso.train(train)

y_norm, y_out = iso.test_set(test_train, outliers)
iso.plot_long_lat(train, test_train, outliers)



