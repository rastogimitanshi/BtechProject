import os
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
import re
import datefinder
from commonregex import CommonRegex
import geograpy
from classify import make_Dictionary
#from postal.parser import parse_address
from classify import train_classifier

def extract_features_for_single_doc(doc_path): 
    features_matrix = np.zeros((1,20), dtype = np.int)
    f=open(doc_path, "r")
    if f.mode == 'r': 
      contents =f.read()
      #print contents

      words = contents.split()
      train_dir = 'travel-nontravel/train-mails'
      dictionary = make_Dictionary(train_dir)
      for word in words:
        wordID = 0
        for i,d in enumerate(dictionary):
          if d[0] == word:
            wordID = i
            features_matrix[0,wordID] = words.count(word)
      
    return features_matrix

def create_label(test_doc):
 # test_doc=['travel-nontravel/tr3.txt']
  list_of_label = []
  for doc_path in test_doc:
    doc_matrix = extract_features_for_single_doc(doc_path)
    model1 = train_classifier()
    result = model1.predict(doc_matrix)
    list_of_label.append(result)
  
  return list_of_label 













