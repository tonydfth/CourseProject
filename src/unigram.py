#This is inspired by a project created by Justin Lizama (jlizama2@illinois.edu) on 09/28/2018 at the University of Illinois at Urbana Champaign


import numpy as np
import math
from tqdm import tqdm
from collections import Counter
import util




def wordProbability(train_set, train_labels, review, laplace):

    index = 0
    numWords = {}
    totCount = 0
    for doc in train_set:
        if train_labels[index] != review:
            index += 1
            continue
        index += 1
        for word in doc:
            totCount += 1
            if word in numWords:
                numWords[word] += 1
            else:
                numWords[word] = 1

    totalWords = len(numWords)
    words = {}
    for word in numWords:
        temp = (laplace + numWords[word])/(totCount + (totalWords*laplace))
        words[word] = np.log(temp)


    non = laplace/(totCount + (totalWords*laplace))
    prob = (words, np.log(non))

    return prob

def single(positiveWords, negativeWords, text):

    positive = np.log(0.8)
    negative = np.log(1 - 0.8)
    for word in text:
        if word in positiveWords[0]:
            positive += positiveWords[0][word]
        else:
            positive += positiveWords[1]
        if word in negativeWords[0]:
            negative += negativeWords[0][word]
        else:
            negative += negativeWords[1]
    if positive >= negative:
        return 'This review is positive'
    else:
        return 'This review is negative'


def multiple(positiveWords, negativeWords, dev_set):

    yhats = []
    for doc in tqdm(dev_set,disable=False):
        positive = np.log(0.7)
        negative = np.log(1-0.7)
        for word in doc:
            if word in positiveWords[0]:
                positive += positiveWords[0][word]
            else:
                positive += positiveWords[1]
            if word in negativeWords[0]:
                negative += negativeWords[0][word]
            else:
                negative += negativeWords[1]
        if positive >= negative:
            yhats.append(1)
        else:
            yhats.append(0)
    pos = 0
    neg = 0
    for i in yhats:
        if i == 1:
            pos = pos+1
        if i == 0:
            neg = neg+1
    if pos > neg:
        decision = "positively reviewed"
    else:
        decision = "negatively reviewed"
    return pos, neg, decision
