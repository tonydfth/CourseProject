#This includes functions to load the dataset
#Attributions to the University of Illinois at Urbana-Champaign
#Some of this code is inspired by/copied from Justin Lizama (jlizama2@illinois.edu) on 09/28/2018.

from os import listdir
import numpy as np
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from tqdm import tqdm

porter_stemmer = PorterStemmer()
tokenizer = RegexpTokenizer(r'\w+')
bad_words = {'aed', 'oed', 'eed'}  # these words fail in nltk stemmer algorithm


def loadSingle(name, stemming, lower_case, silently=False):
    text = []
    f = open(name, 'rb')
    for line in f:
        if lower_case:
            line = line.decode(errors='ignore').lower()
            text += tokenizer.tokenize(line)

        else:
            text += tokenizer.tokenize(line.decode(errors='ignore'))
    if stemming:
        for i in range(len(text)):
            if text[i] in bad_words:
                continue
            text[i] = porter_stemmer.stem(text[i])
    return text


def loadDir(name, stemming, lower_case, silently=False):
    # Loads the files in the folder and returns a list of lists of words from
    # the text in each file

    X0 = []
    count = 0
    for f in tqdm(listdir(name), disable=silently):

        fullname = name + f
        text = []
        with open(fullname, 'rb') as f:
            for line in f:
                if lower_case:
                    line = line.decode(errors='ignore').lower()
                    text += tokenizer.tokenize(line)

                else:
                    text += tokenizer.tokenize(line.decode(errors='ignore'))
        if stemming:
            for i in range(len(text)):
                if text[i] in bad_words:
                    continue
                text[i] = porter_stemmer.stem(text[i])
        X0.append(text)
        count = count + 1
    return X0

def load_trainingset(train_dir, stemming=False, lower_case=False, silently=False):
    X0 = loadDir(train_dir + '/pos/',stemming, lower_case, silently)
    X1 = loadDir(train_dir + '/neg/',stemming, lower_case, silently)
    X = X0 + X1
    Y = len(X0) * [1] + len(X1) * [0]
    Y = np.array(Y)

    return X,Y
