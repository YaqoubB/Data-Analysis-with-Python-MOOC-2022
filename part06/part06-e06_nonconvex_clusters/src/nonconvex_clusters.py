#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    data = pd.read_csv("src/data.tsv", sep="\t") 
    X, y = data[['X1','X2']], data['y']
    k, cl_size = np.arange(0.05, 0.2, 0.05), len(np.unique(y))
    eps, Score, Clusters, Outliers = [], [], [], []
    for i in k:
        model = DBSCAN(eps=i)
        model.fit(X)

        mask = model.labels_ == -1
        lbl = len(np.unique(model.labels_[~mask]))

        eps.append(i), Clusters.append(lbl), Outliers.append(sum(mask))

        if lbl != cl_size:
            Score.append(np.nan)
        else:
            permutation = find_permutation(cl_size, y, model.labels_)
            new_labels = np.array([ permutation[label] for label in model.labels_])
            acc = accuracy_score(y[~mask], new_labels[~mask])
            Score.append(acc)

    arr = np.array([eps, Score, Clusters, Outliers]).T
    return pd.DataFrame(arr, columns = ['eps', 'Score', 'Clusters', 'Outliers'])

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
