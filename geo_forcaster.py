from common import load_file_forcaster
#from common import series_to_supervised
#from pandas import DataFrame
import numpy as np
from sklearn.model_selection import train_test_split
from hmmlearn.hmm import GaussianHMM

class Forcaster:
    def __init__(self, file_name, n_hidden_states=4, test_size_mult=0.5, shuf=False, preprocess=True, latency_days=5):
        tupe = load_file_forcaster(file_name)

        if preprocess:
            tupe = self.preprocess(tupe)

        # tupe sub zero is the time in sorted order of occurance
        self._X = tupe[0]

        # Y tupe sub 1 is the actual points of the location in x,y,z format ftm
        self._Y = tupe[1]

        self._train_data, self._test_data = train_test_split(
            self._Y, test_size=test_size_mult, shuffle=shuf)

        self._hmm = GaussianHMM(n_components=n_hidden_states)
        self.n_latency_days = latency_days

    def test_data(self):
        return self._test_data

    def fit_data(self):
        first_column = self._Y[:,0]
        second_column = self._Y[:,1]
        third_column = self._Y[:,2]
        feature_vector = np.column_stack((first_column, second_column, third_column))
        self._hmm.fit(feature_vector)

    def preprocess(self, tupe):
        sorted_geo_coords = [x for _, x in sorted(zip(tupe[1], tupe[0]))]
        sorted_geo_coords_array = np.array(sorted_geo_coords)
        ordered_times = np.sort(tupe[1])
        print('Shape ' + str(sorted_geo_coords_array.shape))
        return (ordered_times, sorted_geo_coords_array)

    def find_single_likly(self, day_index=10):
        previous_data_start_index = max(0, day_index - self.n_latency_days)

        previous_data_end_index = max(0, day_index - 1)

        previous_data = self._test_data[previous_data_start_index:previous_data_end_index]

        outcome_list = []
        count = 0
        for location in self._Y:
            count = count + 1
            #print(str(count) + ' Prev data is ' + str(previous_data) + ' location is ' + str(location))
            observation = np.row_stack((previous_data, location))
            #print('Observation ' + str(observation))
            outcome_list.append(self._hmm.score(observation))
            #print('Outcome list is ' + str(outcome_list))

        most_probable_outcome = self._Y[np.argmax(outcome_list)]
        final_eval = np.row_stack((previous_data, most_probable_outcome))
        return (previous_data, self._hmm.score(final_eval), most_probable_outcome)

def main():
    print('Starting')
    f = Forcaster('geo_small_csv.txt')
    f.fit_data()

    for i in range(8, len(f.test_data())):
        tupe = f.find_single_likly(i)
        print('Predicted for ' + str(tupe[0]) + ' is probability ' + str(tupe[1]) + ' with answer ' + str(tupe[2]))

    #raw = DataFrame()
    #raw['x'] = [x[0] for x in f.data()]
    #raw['y'] = [x[1] for x in f.data()]
    #raw['z'] = [x[2] for x in f.data()]

    #values = raw.values
    #print('Values ' + str(values))
    #data = series_to_supervised(values)
    #print(data)
    print('Done')

if __name__== '__main__':
    main()
