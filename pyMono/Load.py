import csv
import pandas as pd
from pyMono.Isotherm import Isotherm


def load(path, p0=1, nist_csv=False):
    isotherm = Isotherm([], [])

    try:
        if nist_csv:
            if path.endswith('.xlsx'):
                raise TypeError("The file extension must be .csv if nist_csv is True")
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
            if path.endswith('.csv'):
                raise TypeError("The file extension must be .xlsx if nist_csv is False")
            file = pd.read_excel(path, usecols='A,B')
            if file.columns[0] != 'A' or file.columns[1] != 'B':
                raise ValueError("The input file must have columns A,B")
                isotherm.p = file[str(file.columns[0])].tolist()
                isotherm.q = file[str(file.columns[1])].tolist()
            else:
                return 'File not readable'
            return isotherm
    except FileNotFoundError:
        raise FileNotFoundError("File not found")



