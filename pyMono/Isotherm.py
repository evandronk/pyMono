import matplotlib.pyplot as plt


class Isotherm:
    p = list
    q = list

    def __init__(self, p, q):

        if not isinstance(p, list):
            raise TypeError('p must be a list')

        if not isinstance(q, list):
            raise TypeError('q must be a list')

        self.p = p
        self.q = q

    def plot(self):
        plt.scatter(self.p, self.q)
        plt.show()
