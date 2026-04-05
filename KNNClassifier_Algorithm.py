####Data Mining -- Task2 Classification using KNN #######

import numpy as np
from collections import Counter
from scipy.stats import mode


class KNNClassifier:
    def __init__(self, k_neighbors):
        self.k_neighbors = k_neighbors
        self.X = None
        self.y = None

    def fit(self, X, y):
        self.X_train = X #input features providing for training
        self.y_train= y   # assign labels to training

        return self

    def predict(self, X):
        predict_label= []
        for j in range(len(X)):
            pred=self.KNN(self.k_neighbors, X[j], self.X_train, self.y_train)
            predict_label.append(pred)

        return predict_label

    def findclass(self, distances, k):

        s = False
        while (s == False):
            distance = dict(sorted(distances.items(), key=lambda item: item[0]))
            label_values = list(distance.values())
            nearest_label = label_values[:k]
            modeOfLabels = Counter(nearest_label)
            countOfEach = list(modeOfLabels.values())
            unique_counts = np.unique(np.array(countOfEach))
            if k == 1 or len(countOfEach) == unique_counts.size:
                mode_array = mode(nearest_label, keepdims=True)
                s = True
                return mode_array[0][0]
            else:
                k = k-1



    def KNN(self, k, test_data_point, train_data, train_label):
        distances = {}
        for i in range(len(train_data)):
            a = self.eulidean_distance(train_data[i],test_data_point)
            distances[a] = train_label[i]

        labels = self.findclass(distances, k)
        return labels


    def eulidean_distance(self, x, y):
        return np.sqrt(np.sum((x-y)**2))