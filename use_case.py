from isolation_forest import IsoForest

class UseCase:
    def __init__(self):
        self.iso = IsoForest('pol_recent_geo_location_dataset_small.dat', 12)

    def set_target(self, name):


name = 'h'
uc = UseCase()
uc.set_target(name)
