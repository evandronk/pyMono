import csv
import pandas as pd
import matplotlib.pyplot as plt


class Isotherm:
    p = list
    q = list

    def __init__(self, p, q):
        self.p = p
        self.q = q


def load(path, p0=1, nist_csv=False):
    isotherm = Isotherm([], [])
    if nist_csv:
        with open(path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for column in csv_reader:
                try:
                    if column[0].split(",")[0] == 'pressure':
                        isotherm.p.append(float(column[1].split(",")[0])/p0)
                    if column[0].split(",")[0] == 'adsorption':
                        isotherm.q.append(float(column[1].split(",")[0]))
                except IndexError or ValueError or TypeError:
                    pass
        return isotherm
    else:
        file = pd.read_excel(path, usecols='A,B')
        if type(file.columns[0]) is str:
            isotherm.p = file[str(file.columns[0])].tolist()
            isotherm.q = file[str(file.columns[1])].tolist()
        else:
            return 'File not readable'
        return isotherm


def plot(isotherm):
    plt.scatter(isotherm.p, isotherm.q)
    plt.show()



