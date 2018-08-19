import numpy as np
from sklearn import datasets
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

print(datasets.load_boston().DESCR)

np.random.seed(42)  # constant seed for reproducibility
houses = datasets.load_boston()
split = 4 * len(houses.data) // 5
X_train, X_test = houses.data[:split], houses.data[split:]
y_train, y_test = houses.target[:split], houses.target[split:]
# linear regression works better with normalized features
scaler = StandardScaler() 
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
predictor = SGDRegressor(loss="squared_loss")
predictor.fit(X_train, y_train)
mse = mean_squared_error(y_test, predictor.predict(X_test))
print("Test Mean Squared Error: ${:,.2f}".format(mse * 1000))
