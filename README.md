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
- main.py
The main driver of this application.
- unigram.py
This includes all the algorithms used to produce the unigram model and performs the sentiment analysis on the reviews
- util.py
This includes the functions used to load all the data used

### main.py

### unigram.py

### util.py


## Usage Documentation
