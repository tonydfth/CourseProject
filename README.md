# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.

# Project Documentation

The purpose of this project is to train a binary sentiment classifier using the Naïve Bayes algorithm. At the end, a unigram model will be produced that has the ability to identify if a single review is positive/negative, or if something is positively/negatively reviewed based on a collection of reviews.


## Overview of Functions

This application can be used to perform sentimental analysis on reviews found on the internet. When considering a new product or service, the first thought people have is usually to read some reviews online, then form a sentiment towards it. If the specific product/service is popular enough, there are likely more than thousands of reviews online. This application processes reviews and performs sentiment analysis on them. There are two modes in this application, single review mode and collection review mode.

### Single Review Mode

Single review mode is used to identify if one specific review is positive or negative. In this case, the input of the application would be a block of text, and the output is a binary statement of either positive or negative. 

A possible application for this is to quickly come to a conclusion for long reviews on the internet. For example, this can be used on long review articles online. Rather than reading through it all, one can just copy and paste the text of the article into this application, and get the sentiment of the author right away. 

### Collection Review Mode

Collection review mode is used to determine if a product/service is positively or negatively reviewed. The input is a series of reviews on the specific product/service. The application will go through each review in the collection, and output the number of positive and negative reviews, and give out a binary conclusion on whether this product/service is positively or negatively reviewed based on the number of positive and negative reviews. 

This can be used to obtain the public’s opinion on the desired product/service. For example, rather than reading through all the reviews on IGN for a particular game, one can input every review into this application and obtain the overall sentiment of the game. 


## Implementation Documentation

There are three main files in the source code:
- main.py: The main driver of this application.
- unigram.py: This includes all the algorithms used to produce the unigram model and performs the sentiment analysis on the reviews.
- util.py: This includes the functions used to load all the data used.

### main.py

main.py is called in order to run the application. When calling this function, the mode, training set, and documents to be reviewed can be specified through in-line commands. The program first trains the unigram model using the training set. Depend on which mode is selected, the program then performs the desired tasks on the documents selected.

### unigram.py

The application will first take in the training set and its corresponding labels to generate two lists of words. One for the probability of words that show up in the negative reviews, and another one for positive reviews. Those two lists and are then used to match with each word in the input reviews to determine if a particle review is more positive or negative.
```
wordProbability(train_set, train_labels, review, laplace)
```
This function takes in the documents used for training and the predetermined labels that classifies them as a positive or negative review. This function is ran twice, once for positive reviews and one for negative reviews. For each list, the probability of the word showing up in a review of the specified sentiment is recorded. The probability for unseen words is also stored. Laplace smoothing is used to get more accurate data.


### util.py


## Usage Documentation
