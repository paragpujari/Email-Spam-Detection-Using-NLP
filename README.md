# Email Spam Detection System - A Natural Learning Processing Approach
## Overview
Email spam detection is the process of filtering out unwanted or unsolicited emails, commonly known as spam, from legitimate emails (ham). This task is typically achieved using machine learning algorithms, rule-based methods, or a combination of both. The process involves analyzing the content, headers, and metadata of emails to identify patterns or features indicative of spam, such as certain keywords, suspicious links, or unusual sender behavior. Techniques like Naive Bayes, Support Vector Machines, and deep learning are widely used for building spam classifiers. Spam detection systems aim to enhance user experience by reducing inbox clutter and protecting against potential threats like phishing attacks and malware, while striving to minimize false positives to avoid misclassifying legitimate emails.


In this project,  we are using two Machine Learning models named as Logistic Regression and Support Vector Machines in detecting whether the particular person has diabetes or not based on the heath conditions provided in the dataset.

## Objective:
The main motto of this project is to  detect whether the email is spam or ham.

## Problem Statement:
Email spam detection is the process of filtering out unwanted or unsolicited emails, commonly known as spam, from legitimate emails (ham). Detecting the spam messages from ham  at an early stage can serve as potential indicators of saving our emails, which is crucial in our fight against the hackers. Therefore, to detect whether the email is spam or not, we aim to use two natural language techniques names as Count Vectorizer and Tfidfvectorizer for vectorizing the text into numbers and then applying various machine learning algorithms to detect whether the email is spam or not.

## Dataset:

There are total 5572 records of the email texts in the dataset. From this records, there are total one input features('Text') and one Output feature ('Target')

1.    Text                           --------->   Message Text
2.    Target                         --------->   Type of the Message Text 

## Approach

1.  First the diabetes dataset is obtained.
2.  Then the dataset is cleaned and preprocessed.
3.  The dataset is divided into independent(input features) and dependent(output features).
4.  As all the input features in the dataset are in different range, so Standardization is done to keep all the input features in one range.
5.  The dataset is divided into training and testing data.
6.  Two Machine Learning Models(Logistic Regression) and (Support Vector Machines) are used to test the accuracy level of the model.
7.  Using the above two models, the data is first trained, then using the test data, the model is predicted and we get the predicted output for each algorithms.
8.  Then we calculate the accuracy value for each training and testing data for both the models.
9.  The model that has better accuracy will be considered for determining the  diabetic condition of the patient.
10. A prediction system is also built that helps in determining whether the person is having diabetes or not using a test data.
11. Then we have developed the web application for depicting the diabetic condition of the patient.
