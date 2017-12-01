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
#from postal.parser import parse_address
dictionary={}

def make_Dictionary(train_dir):
    emails = [os.path.join(train_dir,f) for f in os.listdir(train_dir)]    
    all_words = []       
    for mail in emails:    
        with open(mail) as m:
            for i,line in enumerate(m):
                if i == 0:
                    words = line.split()
		    
                    all_words += words
    
    dictionary = Counter(all_words)
    
    list_to_remove = dictionary.keys()
    for item in list_to_remove:
        if item.isalpha() == False: 
            del dictionary[item]
        elif len(item) == 1 or len(item)==2 or len(item)==3:
            del dictionary[item]

    dictionary = dictionary.most_common(20)
  
    return dictionary
    
def extract_features(mail_dir): 
    files = [os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(files),20))
    docID = 0;
    for fil in files:
      with open(fil) as fi:
        for i,line in enumerate(fi):
          if i == 0:
            words = line.split()
            for word in words:
              wordID = 0
              for i,d in enumerate(dictionary):

                if d[0] == word:
                  wordID = i
                  features_matrix[docID,wordID] = words.count(word)
        docID = docID + 1     
    return features_matrix

def train_classifier():    
  train_dir = 'travel-nontravel/train-mails'
  dictionary = make_Dictionary(train_dir)

  # Prepare feature vectors per training mail and its labels

  train_labels = np.zeros(100)
  train_labels[50:99] = 1
  train_matrix = extract_features(train_dir)

  # Training SVM and Naive bayes classifier and its variants

  model1 = LinearSVC()
  model2 = MultinomialNB()

  model1.fit(train_matrix,train_labels)
  model2.fit(train_matrix,train_labels)
  return model1

# Create a dictionary of wor



# Test the unseen mails for Spam

#print model1

test_dir = 'travel-nontravel/test-mails'
test_matrix = extract_features(test_dir)
test_labels = np.zeros(60)
test_labels[29:59] = 1
model1=train_classifier()
result1 = model1.predict(test_matrix)
#result2 = model2.predict(test_matrix)


print confusion_matrix(test_labels,result1)
#print confusion_matrix(test_labels,result2)

