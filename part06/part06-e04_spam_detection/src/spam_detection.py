#!/usr/bin/env python3

import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def spam_detection(random_state=0, fraction=1.0):
    with gzip.open('src/ham.txt.gz') as f1, gzip.open('src/spam.txt.gz') as f2:
        h = f1.readlines()
        s = f2.readlines()
        ham = h[:int(len(h)*fraction)]
        spam = s[:int(len(s)*fraction)]
        
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(ham+spam)
    y = np.concatenate((np.zeros(len(ham)), np.ones(len(spam))))
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, test_size=0.25, random_state=random_state)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)
    acc = accuracy_score(y_predict, y_test)
    size = len(y_test)
    misclassified = np.sum(y_predict != y_test)
    print(type(y_test), len(y_predict))
    return acc, size, misclassified

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
