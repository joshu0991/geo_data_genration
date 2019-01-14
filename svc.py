import numpy as np
from sklearn.svm import SVC
from common import load_file

class GeoSVC:
    def __init__(self, data_file):
        self.X, self.Y, = load_file(data_file)
        self.model = SVC(gamma='auto')
        self.model.fit(self)

