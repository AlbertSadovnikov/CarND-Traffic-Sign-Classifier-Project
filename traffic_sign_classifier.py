import pickle
import numpy as np
import pandas as pd
import cv2 as cv


training_file = 'data/train.p'
validation_file = 'data/valid.p'
testing_file = 'data/test.p'

with open(training_file, mode='rb') as f:
    train = pickle.load(f)
with open(validation_file, mode='rb') as f:
    valid = pickle.load(f)
with open(testing_file, mode='rb') as f:
    test = pickle.load(f)

X_train, y_train = train['features'], train['labels']
X_valid, y_valid = valid['features'], valid['labels']
X_test, y_test = test['features'], test['labels']


n_train = X_train.shape[0]
n_test = X_test.shape[0]
image_shape = X_train.shape[1:3]
class_names = pd.read_csv('signnames.csv', index_col=0)
print(class_names)
print(class_names.loc[23]['SignName'])
n_classes = len(class_names)

print("Number of training examples =", n_train)
print("Number of testing examples =", n_test)
print("Image data shape =", image_shape)
print("Number of classes =", n_classes)


