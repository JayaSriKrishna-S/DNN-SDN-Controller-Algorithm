import pickle
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os
from keras.models import model_from_json
sc = pickle.load(open('../S4_upda2/unixscaler_BL5.pkl', 'rb'))

with open("../S4_upda2/Traffic_model_BL5.json", "r") as f:
    unix = model_from_json(f.read())
unix.load_weights("../S4_upda2/Traffic_model_BL5.h5")


dataset = pd.read_csv('sdn_upda2.csv', index_col='TimeStamp', parse_dates=True)
dataset = dataset.drop(['IP Address', 's3', 's5', 'Transfer(s1)',
                       's2', 'Priority', 'Membership'], axis=1)
copy = pd.read_csv("sdn_upda2.csv", index_col='TimeStamp', parse_dates=True)
copy = copy.drop(['IP Address', 's3', 's5', 'Transfer(s1)', 's2',
                 'Priority', 'Membership'], axis=1)
copy = copy.values

dataset = sc.fit_transform(dataset)
real_unixred = dataset[6049:, 0]
real_unix = copy[6049:, 0]
x_test = []
for i in range(6048, 8064):
    x_test.append(dataset[i-50:i, 0])

X_test = np.array(x_test)

X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_unixred = unix.predict(X_test)

predicted_unix = sc.inverse_transform(predicted_unixred)
print(predicted_unix)


xp_test = []
dataset = pd.read_csv("sdn_upda2.csv", index_col='TimeStamp', parse_dates=True)
dataset = dataset.drop(['IP Address', 's3', 's5', 'Transfer(s1)',
                       's2', 'Priority', 'Membership'], axis=1)
dataset = sc.fit_transform(dataset)

predicted_week = []
for i in range(6048, 6048+2016+2016):
    xp_test.append(dataset[i-50:i, 0])
    print(i)
    print(xp_test)
    XP_test = np.array(xp_test)
    XP_test = np.reshape(XP_test, (XP_test.shape[0], XP_test.shape[1], 1))
    predicted_unix = unix.predict(XP_test)
    dataset = np.append(dataset, predicted_unix)
    dataset = np.reshape(dataset, (dataset.shape[0], 1))
    xp_test = []
    predicted_week.append(sc.inverse_transform(predicted_unix))

jsk = []
j = 0
for i in predicted_week:
    jsk.append(predicted_week[j][0][0])
    j = j+1

plt.plot(jsk[2016:], color='blue', label='Real')
plt.legend()
plt.show()
with open("../PRED/S4/S4", "wb") as fp:  # Pickling
    pickle.dump(jsk[2016:], fp)
