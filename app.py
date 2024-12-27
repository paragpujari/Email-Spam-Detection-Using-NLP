# import all the necessary libraries

import numpy as np
import pandas as pd
import streamlit as st
import pickle
import string
import nltk
from   nltk.corpus import stopwords
nltk.download('punkt')
from   nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

# define the function for preprocessing the text

def transform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)

  # remove special characters
  y = []
  for i in text:
    if(i.isalnum()):
      y.append(i)

  text = y[:]
  y.clear()


  # remove stop words and punctuation
  y = []
  for i in text:
    if(i not in stopwords.words('english') and i not in string.punctuation):
      y.append(i)

  text = y[:]
  y.clear()


  # Perform Stemming
  y=[]
  for i in text:
    y.append(ps.stem(i))

  return(" ".join(y))




# open the models in the read mode
tfidf = pickle.load(open('models/vectorizer.pkl','rb'))
model = pickle.load(open('models/model.pkl','rb'))


# set the title of the web page
st.title("Email/SMS Spam CLssifier")

# enter the message
input_msg = st.text_area("Enter the message:")


if(st.button('Predict')):
  # preprocess the text
  transformed_text = transform_text(input_msg)
  # vectorize the text
  vectorized_data = tfidf.transform([transformed_text])
  # predict
  result = model.predict(vectorized_data)[0]
  print(result)
  if result == 1:
    st.header("Spam")
  else:
    st.header("Not Spam")