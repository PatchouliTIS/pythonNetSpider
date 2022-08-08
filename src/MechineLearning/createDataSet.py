from numpy import array
import operator


def createDataset():
    group = array([[1.0, 1.1], [1.1, 1.2], [3.4, 4.5], [4.8, 3.3]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels
