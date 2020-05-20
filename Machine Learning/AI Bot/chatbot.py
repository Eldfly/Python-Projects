# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:25:56 2020

@author: Sofia
"""

import nltk
from nltk import WordNetLemmatizer
import  json
import pickle
import numpy as np
import random
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
from keras.models import load_model
import pickle
nltk.download('punkt')
nltk.download('wordnet')

###############################################################################
########### Date preproccessing ###############################################

lemmatizer = WordNetLemmatizer()

#read json file
data_file = open('intents.json').read()
intents = json.loads(data_file) 

try:
     with open('data.pickle', 'rb') as f:
         words, classes, training_X, training_y = pickle.load(f)
except:

    
    #create list to store the data read from the json file
    words = []
    classes = []
    documents = []
    ignore_words = ['?','!']
    
        
    ##go thorugh the json file and put every item in their right lists.
    for intent in intents['intents']:
        
        for pattern in intent['patterns']:
            
            word =  nltk.word_tokenize(pattern)
                
            words.extend(word)
            documents.append((word, intent['tag']))
            
            if intent['tag'] not in classes:
                classes.append(intent['tag'])
    
    
    '''lemmatize means to turn a word into its base meaning, or its lemma. 
    For example, the words “walking”, “walked”, “walks” all have the same lemma, which is just “walk”. '''
    words = [lemmatizer.lemmatize(w.lower()) for w in words if not w in ignore_words]
    
    ##sort the list, make the words unique in the lists. 
    words = sorted(list(set(words)))
    classes = sorted(list(set(classes)))
    
    #####################################################################################
    ################## CREATE TRAINIGN DATA #############################################
    
    training = []
    output_empty  = [0] * len(classes)
    
    for doc in documents:
        
        bag = []
        
        pattern_words = doc[0]
        
        pattern_words = [lemmatizer.lemmatize(w.lower()) for w in pattern_words]
        
        for word in words:
            bag.append(1) if word in pattern_words else bag.append(0)
        
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        
        training.append([bag, output_row])
        
    random.shuffle(training)
    training = np.array(training)  
    
    training_X = list(training[:, 0])
    training_y = list(training[:, 1])
    
    with open('data.pickle', 'wb') as f:
        pickle.dump(words, classes, training_X, training_y, f)

##############################################################################
########### CREATE MODEL ###############################


model = Sequential()

#Adding input and first hideen layer
model.add(Dense(128, activation="relu", kernel_initializer="uniform", input_dim=len(training_X[0])))
model.add(Dropout(0.5))

#adding second hidden layer 
model.add(Dense(64, activation='relu', kernel_initializer="uniform"))
model.add(Dropout(0.5))

#Adding output layer
model.add(Dense(len(training_y[0]), activation='softmax'))

model.compile(optimizer = 'sgd', loss= 'categorical_crossentropy', metrics = ['accuracy'])

try:
    load_model('chatbot_model.h5')
except:
    hist = model.fit(np.array(training_X), np.array(training_y), epochs=200, batch_size=5, verbose=1)
    model.save('chatbot_model.h5', hist)

    
    with open('words.pkl', 'wb') as f:
       pickle.dump(words, f)
    with open('classes.pkl', 'wb') as f:
       pickle.dump(classes, f)

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result


def chatbot_response():
    
    while True:
        inp = input('You: ')
        if inp == 'quit':
            break
    
        ints = predict_class(inp, model)
        res = getResponse(ints, intents)
        print(res)

chatbot_response()
