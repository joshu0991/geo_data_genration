import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from common import load_file_outliers
from common import load_file_outliers_space_time
from common import load_file_clus
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import LocalOutlierFactor
from sklearn.covariance import EllipticEnvelope

class IsoForest:
    def __init__(self, file_name, max_samples):
        self._X, self._Y= load_file_clus(file_name)
        self._X = self._X.astype(np.float64)
        rng = np.random.RandomState(42)
        self._iso = IsolationForest(behaviour='new', max_samples=max_samples,
                                    random_state=rng, contamination='auto')
        #self._lof = LocalOutlierFactor(novelty=True)

        #self._ecurve = EllipticEnvelope()
        self._Xp, self._Yp = load_file_outliers_space_time(file_name)
        self._Xp = self._Xp.astype(np.float64)
        self._Yp = self._Yp.astype(np.float64)



    def train(self, data):
        self._iso.fit(data)
        #self._iso.fit(data)
        #self._lof.fit(data)
        #self._ecurve.fit(data)

    def test_set_iso(self, normal, outliers, train):
        y_pred_test = self._iso.predict(normal)
        y_pred_outliers = self._iso.predict(outliers)
        y_pred_train = self._iso.predict(train)
        return y_pred_test, y_pred_outliers, y_pred_train

    """
    def test_set_lof(self, normal, outliers, train):
        y_pred_test = self._lof.predict(normal)
        y_pred_outliers = self._lof.predict(outliers)
        y_pred_train = self._lof.predict(train)
        return y_pred_test, y_pred_outliers, y_pred_train
    """
    """
    def test_set_ecurve(self, normal, outliers, train):
        y_pred_test = self._ecurve.predict(normal)
        y_pred_outliers = self._ecurve.predict(outliers)
        y_pred_train = self._ecurve.predict(train)
        return y_pred_test, y_pred_outliers, y_pred_train
    """

    def plot_long_lat_time(self, train, norm, outliers):
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

    def plot_long_lat(self, train, norm, outliers):
        fignum = 1
        fig = plt.figure(fignum, figsize=(4, 3))
        ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

        ax.scatter(train[0], train[1],
                   c='white', edgecolor='k')

        """
        ax.scatter(norm[0], norm[1],
                   c='green', edgecolor='k')

        ax.scatter(outliers[0], outliers[1],
                   c='red', edgecolor='k')
        """
        ax.w_xaxis.set_ticklabels([])
        ax.w_yaxis.set_ticklabels([])
        ax.w_zaxis.set_ticklabels([])
        ax.set_xlabel('longitude')
        ax.set_ylabel('latitude')
        ax.set_zlabel('time')
        ax.dist = 12
        plt.show()

iso = IsoForest('recent_geo_location_dataset_small.dat', 12)

length = len(iso._Xp)
train_length = int(length/2)
outlier_start = length - 6

outliers = iso._Xp[outlier_start:]
train = iso._Xp[0:train_length]
test_train = iso._Xp[train_length:outlier_start]

iso.train(train)

y_norm, y_out, y_train = iso.test_set_iso(test_train, outliers, train)

print('Outliers ' + str(y_out))
print('test ' + str(y_norm))
print('train ' + str(y_train))
#iso.plot_long_lat(y_train, y_norm, y_out)
iso.plot_long_lat_time(y_train, y_norm, y_out)
"""
y_norm, y_out, y_train = iso.test_set_lof(test_train, outliers, train)
print('Outliers ' + str(y_out))
print('test ' + str(y_norm))
print('train ' + str(y_train))

y_norm, y_out, y_train = iso.test_set_ecurve(test_train, outliers, train)
print('Outliers ' + str(y_out))
print('test ' + str(y_norm))
print('train ' + str(y_train))
iso.plot_long_lat(train, test_train, outliers)
"""




