# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:22:38 2020

@author: Sofia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, Flatten, MaxPool2D, Conv2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('train.csv')

X = df.drop('label', axis=1).values
y = df['label'].values


#reshape the data for images
X = X.reshape(42000,28,28,1)
X = X/255

#Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

##create categorical values for my output
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)



#Create model and train it
model = Sequential()

model.add(Conv2D(filters=32, kernel_size=(4,4), activation='relu', input_shape=(28,28,1)))
model.add(MaxPool2D(2,2))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=25)

model.fit(x=X_train, 
          y=y_train_cat, 
          epochs=10, 
          validation_data=(X_test, y_test_cat), 
          callbacks=[early_stop])

###Evaluate model before prediction
metrics = pd.DataFrame(model.history.history)
metrics[['loss', 'val_loss']].plot()
metrics[['accuracy', 'val_accuracy']].plot()
model.evaluate(X_test, y_test_cat, verbose=0)

####Predict and evaluate prediction

y_pred = model.predict_classes(X_test)

##Validate
df_validate = pd.read_csv('test.csv')
X_valid = np.array(df_validate)
X_valid = X_valid.reshape(28000,28,28,1)
X_valid = X_valid/255


prediction = model.predict_classes(X_valid)

output = pd.DataFrame({'ImageId': list(df_validate.index.values+1) , 'Label': prediction})
output.to_csv('my_submission.csv', index=False)
