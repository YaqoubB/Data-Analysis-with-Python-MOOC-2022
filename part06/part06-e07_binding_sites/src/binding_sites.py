#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc
import scipy

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def toint(x):
    dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return dic[x]

def get_features_and_labels(filename):
    data = pd.read_csv(filename, sep="\t")
    X = data['X'].apply(lambda x: list(map(toint, x)))
    X = np.array(X.values.tolist())
    y = data['y']
    return X, y

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(linkage='average', affinity='euclidean', n_clusters=2)
    model.fit(X)
    permutation = find_permutation(2, y, model.labels_)
    new_labels = [ permutation[label] for label in model.labels_]
    acc = accuracy_score(y, new_labels)
    return acc

def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    D = pairwise_distances(X, metric='hamming')
    model = AgglomerativeClustering(linkage='average', affinity='precomputed', n_clusters=2)
    model.fit(D)
    permutation = find_permutation(2, y, model.labels_)
    new_labels = [ permutation[label] for label in model.labels_]
    acc = accuracy_score(y, new_labels)
    #plot(D, method='average', affinity='hamming')
    return acc


def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()