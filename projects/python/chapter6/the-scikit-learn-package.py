from sklearn import datasets

iris = datasets.load_iris()

print(iris.feature_names) # columns
print(iris.data[:5]) # first 5 rows of the ndarray
print('...')
print(iris.DESCR) # description
