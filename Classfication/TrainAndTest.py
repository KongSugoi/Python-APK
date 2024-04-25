from random import random
from sklearn.model_selection import train_test_split
import numpy as np
from RandomForest import RandomForest
import pandas as pd

# Get data

# Get data from file csv
data_file = pd.read_csv("path_to_file")

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

acc = accuracy(y_test, predictions)
print("RandomForest classfication accuracy: ", acc)

# classfication
input_value = list(map(int, input().split))
x = np.array(input_value)
result = clf.predict(x)
print(result)