# coding: utf-8
__author__ = 'liza'

import codecs
import numpy as np
from sklearn import linear_model

print 'Reading tables...'

tags = codecs.open('tag_taggers3.csv', 'r', 'utf-8').readlines()
lemmas = codecs.open('lemma_taggers.csv', 'r', 'utf-8').readlines()
pos = codecs.open('pos_taggers.csv', 'r',' utf-8').readlines()

print 'Collecting data for tags...'
train = []
for line in tags[1:150000]:
    line = line.strip()
    values = line.split('\t')[3:]
    #print values
    now = []
    for v in values:
        print v
        now.append(int(v))
    train.append(now)
print train

#tag_train = np.array([[int(l) for l in line.split('\t')[3:]] for line in tags[1:150000]])
tag_train = np.array(train)
labels = []
for line in tags[1:150000]:
    right1, right2 = line.split('\t')[1], line.split('\t')[2]
    if right1 == '1' and right2 == '1':
        label = 1
    elif right1 == '0' and right2 == '0':
        label = 2
    elif right1 == '1' and right2 == '0':
        label = 3
    elif right1 == '0' and right2 == '1':
        label = 4
    labels.append(label)

print 'Training...'

tag_labels = np.array(labels)
clf = linear_model.SGDClassifier()
clf.fit(tag_train, tag_labels)
tag_test = np.array([line[3:] for line in tags[150000:]])
print clf.predict(tag_test)
