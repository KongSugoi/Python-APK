from random import random
from sklearn.model_selection import train_test_split
import numpy as np
from RandomForest import RandomForest
import pandas as pd
# Get data

# Get data from file csv
data_file = pd.read_csv("C:/Users/Admin/Downloads/Python-APK-master/Classfication/convert_done.csv")

# Split features(X) và labels (y) 
X = data_file.iloc[:, :-1].values # lấy tất cả hàng : và lấy các cột từ đầu đến cuối nhưng không lấy cái cuối :-1
y = data_file.iloc[:,-1].values # lấy tất cả các hàng của cột -1 (là cột cuối cùng)

# train and test accuracy:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

clf = RandomForest(n_trees=20)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

acc =  accuracy(y_test, predictions)
print("Accuaracy: ",acc)

file = input("Path to file vector: ")
data_file = pd.read_csv(file)
X = data_file.iloc[1,1:].values
prediction = clf.predict(X)
if prediction==1: print("This is malware")
else: print("This is not malware")
