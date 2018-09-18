import numpy as np
from sklearn import datasets
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score

# constant seed to reproduce the same results every time
np.random.seed(28) 

iris = datasets.load_iris()
# prepare labels for binary classification task
# 1 iff original target is Iris-Versicolor
labels = iris.target == 1 
labels = labels.reshape((len(labels), 1))
data = np.append(iris.data, labels, axis=1) 
# randomly shuffle data and split to train and test sets
data = np.random.permutation(data)
split = 4 * len(data) // 5
train_data, test_data = data[:split], data[split:]
train_features = train_data[:, :-1]
train_labels = train_data[:, -1]
predictor = SGDClassifier(n_iter=500)
predictor.fit(train_features, train_labels)
test_features = test_data[:, :-1]
test_labels = test_data[:, -1]
test_error = 1 - accuracy_score(test_labels, 
	predictor.predict(test_features))
print("Test Error: {:.3%}".format(test_error))
