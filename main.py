import pandas as pd
import numpy as np

class ind_place:
    def __init__(self):
        self.data = pd.read_csv('Places.csv')['Places']
        self.data_list = np.unique([i.lower() for i in self.data])
        print("__Data loaded__")

    def check(self, place):
        """check if the word is a city from India"""
        return True if place.lower() in self.data_list else False

    def add_place(self, new_places_list):
        """add new place names to the existing list"""
        pass

if __name__ == '__main__':
    c = ind_place()
    print(c.check('Bangalore'))

