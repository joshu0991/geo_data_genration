import numpy as np
from sklearn.svm import SVC

class GeoSVC:
    def __init__(self, data_file):
        self.X, self.Y, = load_file(data_file)
        self.model = SVC(gamma='auto')
        self.model.fit(self)
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
