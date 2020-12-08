import os
from pandas import DataFrame
import glob

class Ampule:
    def __init__(self, py_path, dep_path, pdf_path):
        self.py_path = py_path.replace(' ', '\ ')
        self.dep_path = dep_path.replace(' ', '\ ')
        self.pdf_path = pdf_path.replace(' ', '\ ')
        self.dat_paths = set()

    def load(self, dat_path):
        self.dat_paths.update([dat_path.replace(' ', '\ ')])
        with open(dat_path) as f:
            names = f.readline()[2:].split()
            raw_columns = zip(*(map(float, line.split()) for line in f))
            return DataFrame({name: col for name, col in zip(names, raw_columns)})

    def __del__(self):
        with open(self.dep_path, 'w') as deps:
            print(self.pdf_path + ":", self.py_path, end = ' ', file = deps)
            for dat_path in self.dat_paths:
                print(dat_path, end = ' ', file = deps)
            print(file = deps)
            print(file = deps)
            for dat_path in self.dat_paths:
                print(dat_path + ":", file = deps)
                print(file = deps)

def search_mask(pref, suff = None, cls = int, key_ordering = lambda x: x):
    if not suff:
        mask = pref + '*'
        sl = slice(len(pref), None)
    else:
        mask = pref + '*' + suff
        sl = slice(len(pref), -len(suff))
    return sorted(((p, cls(p[sl])) for p in glob.glob(mask)), key = lambda x: key_ordering(x[1]))
