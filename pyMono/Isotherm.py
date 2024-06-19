import matplotlib.pyplot as plt


class Isotherm:
    p = list
    q = list

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def plot(self):
        plt.scatter(self.p, self.q)
        plt.show()