# Email Spam Detection System - A Natural Learning Processing Approach
## Overview
Email spam detection is the process of filtering out unwanted or unsolicited emails, commonly known as spam, from legitimate emails (ham). This task is typically achieved using machine learning algorithms, rule-based methods, or a combination of both. The process involves analysing the content, headers, and metadata of emails to identify patterns or features indicative of spam, such as certain keywords, suspicious links, or unusual sender behaviour. Techniques like Naive Bayes, Support Vector Machines, and deep learning are widely used for building spam classifiers. Spam detection systems aim to enhance user experience by reducing inbox clutter and protecting against potential threats like phishing attacks and malware, while striving to minimize false positives to avoid misclassifying legitimate emails.


In this project, we aim to use two natural language techniques names as Count Vectorizer and Tfidfvectorizer for vectorising the text into numbers and then applying various machine learning algorithms to detect whether the email is spam or not.


## Objective:
The main motto of this project is to  detect whether the email is spam or ham.

## Problem Statement:
Email spam detection is the process of filtering out unwanted or unsolicited emails, commonly known as spam, from legitimate emails (ham). Detecting the spam messages from ham  at an early stage can serve as potential indicators of saving our emails, which is crucial in our fight against the hackers. Therefore, to detect whether the email is spam or not, we aim to use two natural language techniques names as Count Vectorizer and Tfidfvectorizer for vectorizing the text into numbers and then applying various machine learning algorithms to detect whether the email is spam or not.

## Dataset:

There are total 5572 records of the email texts in the dataset. From this records, there are total one input features('Text') and one Output feature ('Target')

1.    Text                           --------->   Message Text
2.    Target                         --------->   Type of the Message Text 

## Approach

1.  First the email dataset is obtained.
2.  Then the dataset is cleaned and preprocessed.
3.  Then Exploratory Data Analysis(EDA) is performed on the dataset and we have formed three new columns named as 'number_of_characters', 'number_of_words','number_of_sentences'. Then we have performed statistical analysis on it.
4.  Text Data is preprocessed where it is converted into lower case and all the special characters has been removed from it. Stop words , punctuations has been removed and the stemming has been done to bring out the correct root words.
5.  Count Vectorizer and tfidf vectorizer is performed on the preprocessed data where the text is converted into the numbers.
6.  Various Machine Learning algorithms has been applied on the vectorized data , so that the models can be easily be trained on the data and we can easily get the accuracy and the precision scores.
7.  For improving the accuracy of the model, votingclassifier and StackClassifier has been applied on the dataset so that the accuracy of the model can be imporved.
8.  Files has been created for the objects of tfidf and mnb so that we can use these files while developing the website to predict the type of text message.
9.  Then we have developed the web application for determining whether the email is spam or not.
10.  Here from this project, Multinomial Naive Bayes is considered for this project as it has the highest score.

## ALGORITHMS USED:

1.  Gaussian Naive Bayes
2.  Multinomial Naive Bayes
3.  Bernoulli Naive Bayes
4.  Logistic Regression
5.  Support Vector Machines
6.  Multinomial Naive Bayes
7.  Decision Tree Classifier
8.  K Neighbors Classifier
9.  Random Forest Classifier
10. Ada Boost Classifier
11. Bagging Classifier
12. Extra Trees Classifier
13. Gradient Boosting Classifier
14. XGB Classifier


## HYPER PARAMETERS USED:

1. kernel
2. gamma
3. max_depth
4. solver
5. penalty
6. n_estimators
7. random_state
8. probability
9. voting
10. estimators
11. final_estimator

## OUTPUT:

1. Gaussian Naive Bayes

   a.  accuracy_score  = 86.94390715667312
   
   b.  precision_score = 0.5068493150684932


3. Multinomial Naive Bayes

   a. accuracy_score =  97.09864603481626
   
   b. precision_score = 1.0

5. Binomial Naive Bayes

   a. accuracy_score = 98.35589941972921
   
   b. precision_score = 0.991869918699187

7. Voting Classifier

   a. accuracy_score = 98.16247582205028
   
   b. precision_score = 0.9917355371900827

9. Stacking Classifier

   a. accuracy_score = 97.87234042553192
   
   b. precision_score = 0.9393939393939394
