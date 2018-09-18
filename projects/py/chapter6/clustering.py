import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import *

iris = datasets.load_iris()
# instead of running the algorithm many times with random
# initial values for centroids, we picked one that works well;
# the values below were obtained from one of the random runs:
centroids = np.array([
  [5.006, 3.418, 1.464, 0.244],
  [5.9016129, 2.7483871, 4.39354839, 1.43387097],
  [6.85, 3.07368421, 5.74210526, 2.07105263],
])
predictor = KMeans(n_clusters=3, init=centroids, n_init=1)
predictor.fit(iris.data)
# range of scores is [0.0, 1.0]; the higher, the better
completeness = completeness_score(iris.target, predictor.labels_)
homogeneity = homogeneity_score(iris.target, predictor.labels_)
accuracy = accuracy_score(iris.target, predictor.labels_)
print("Completeness:", completeness)
print("Homogeneity:", homogeneity)
print("Accuracy:", accuracy)
