import random
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

def find_file(path):
    with open(path) as file:
        for line in file:
            yield line

def read_data(filename):
    X = []
    Y = []
    XX = []
    YY = []
    data = []
    for line in find_file(filename):
        content = line.strip().split()
        content = list(map(int, content))
        if content[-1] > 0:      #  >20
            data.append(content)

    size = len(data)
    rs = random.sample(range(0,size), int(size * 0.7))
    for item in rs:
        X.append(data[item][:-1])
        Y.append([data[item][-1]])

    for i in range(0, size):
        if i not in rs:
            XX.append(data[i][:-1])
            YY.append([data[i][-1]])
    return X, Y, XX, YY, rs, data

filename = 'data.csv'
X_train, y_train, X_test, y_test, rs, data = read_data(filename)

X_scaler = StandardScaler()
y_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
y_train = y_scaler.fit_transform(y_train)
X_test = X_scaler.transform(X_test)
y_test = y_scaler.transform(y_test)

regressor = SGDRegressor(loss='squared_loss')
scores = cross_val_score(regressor, X_train, y_train, cv=5)
print('交叉验证R方值:', scores)
print('交叉验证R方均值:', np.mean(scores))
regressor.fit(X_train, y_train)
print('测试集R方值:', regressor.score(X_test, y_test))
print(regressor.coef_)
print(regressor.intercept_)

print(len(rs))
# predictions = regressor.predict(X_test)
# for i, prediction in enumerate(predictions):
#     print('Predicted: %s, Target: %s' % (prediction, y_test[i]))
p_result = []
r_result = []
for i in range(4606):
    if i not in rs:
        y_pre = 0.27459226 * data[i][0] + 0.15087893 * data[i][1] + 0.12574229 * data[i][2] + 0.24191116 * data[i][3] \
                + 0.23476721 * data[i][4] - 0.00016903
        y_real = data[i][5]
        p_result.append(y_pre)
        r_result.append(y_real)
plt.plot(range(len(p_result)),p_result,color='red',label='predict')
plt.plot(range(len(r_result)),r_result,color='green',label='real')
plt.xlabel('The product_parent serial number')
plt.ylabel('Sales amount')
plt.title('Fitted value by our pattern')
plt.legend(loc=0)
plt.show()

print(p_result)
print(r_result)

