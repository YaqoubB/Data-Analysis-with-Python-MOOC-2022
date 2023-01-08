#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    X,y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, test_size=0.20, random_state=0)
    model = naive_bayes.GaussianNB()
    model.fit(X_train, y_train)
    labels_fitted = model.predict(X_test)
    acc = metrics.accuracy_score(labels_fitted, y_test)
    return acc

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
