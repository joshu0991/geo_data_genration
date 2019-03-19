from common import load_file

class NewmanCluster:
    def __index__(self, file_name):
        self.X, self.Y, = load_file(data_file)