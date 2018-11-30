from sklearn.datasets import load_iris

from dislib.classification import RandomForestClassifier
from dislib.data import Dataset, Subset

import numpy as np


def main():

    x, y = load_iris(return_X_y=True)
    subset_1 = Subset(x[:len(x) // 2], y[:len(x) // 2])
    subset_2 = Subset(x[len(x) // 2:], y[len(x) // 2:])
    iris_ds = Dataset(4)
    iris_ds.append(subset_1)
    iris_ds.append(subset_2)

    forest = RandomForestClassifier(10)
    forest.fit(iris_ds)

    test_subset_1 = Subset(x[:len(x) // 2])
    test_subset_2 = Subset(x[len(x) // 2:])
    test_ds = Dataset(4)
    test_ds.append(test_subset_1)
    test_ds.append(test_subset_2)
    prediction = forest.predict(test_ds)
    test_ds.collect()

    labels = []
    for subset in prediction:
        labels.append(subset.labels)
    y_pred = np.concatenate(labels)

    print('y:')
    print(y)
    print('y_pred:')
    print(y_pred)


if __name__ == "__main__":
    main()
