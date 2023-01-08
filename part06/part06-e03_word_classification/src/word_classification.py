#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
import re

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    vectorizer = CountVectorizer(vocabulary=list(alphabet), tokenizer=lambda x: [*x])
    X = vectorizer.fit_transform(a)
    return X

def contains_valid_chars(s):
    if re.match(r'^[äö\-a-zA-Z]*$', s):
        return True
    return False


def get_features_and_labels():
    fin = list(map(str.lower, load_finnish())) 
    fin = list(filter(contains_valid_chars, fin))

    eng = [x for x in list(load_english()) if re.match(r'^[a-z]+', x)] 
    eng = list(map(str.lower, eng))
    eng = list(filter(contains_valid_chars, eng))

    X = get_features(fin + eng)
    y_fin, y_eng = np.zeros(len(fin)), np.ones(len(eng))
    y = np.concatenate((y_fin, y_eng))
    return (X, y)


def word_classification():
    features, labels = get_features_and_labels()
    model = MultinomialNB()
    scores = cross_val_score(model, features, labels, cv=model_selection.KFold(n_splits=5, shuffle=True, random_state=0))
    return scores


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()

