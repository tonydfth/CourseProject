#This is inspired by a project created by Justin Lizama (jlizama2@illinois.edu) on 09/28/2018 at the University of Illinois at Urbana Champaign


import argparse
import unigram as uni
import util


def main(args):
    train_set, train_labels= util.load_trainingset(args.training_dir, True, True, False)
    positiveWords = uni.wordProbability(train_set, train_labels, 1, 0.001)
    negativeWords = uni.wordProbability(train_set, train_labels, 0, 0.001)
    if args.development_dir == 'none':
        print('Please define development set')
        return
    if args.mode == "single":
        text = util.loadSingle(args.development_dir, True, True, True)
        print(uni.single(positiveWords, negativeWords, text))
    elif args.mode == "multiple":
        dev = util.loadDir(args.development_dir, True, True)
        pos, neg, decision = uni.multiple(positiveWords, negativeWords, dev)
        print('Number of positive reviews:', pos)
        print('Number of negative reviews:', neg)
        print('The movie is: ', decision)
    else:
        print('Select either single review mode or multiple review mode')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Course Project for CS410: Sentiment Analysis for Video game reviews')
    parser.add_argument('--mode', dest="mode", type=str, default = 'none', help='Select either single review mode or multiple review mode')
    parser.add_argument('--training', dest='training_dir', type=str, default='data/reviews/train',
                        help='the directory of the training data')
    parser.add_argument('--source', dest='development_dir', type=str, default='none',
                        help='the directory/file of the development data')

    args = parser.parse_args()
    main(args)
