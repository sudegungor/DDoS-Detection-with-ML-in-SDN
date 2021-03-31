from sklearn import tree
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
veriler = pd.read_csv('BakalımOlmusMu.csv')
Y = veriler['outcome']
X = veriler.drop(columns=['outcome'])

#işlemler numpy dizileri üzerinden işleyeceği için
x = X.values
y = Y.values

dt = tree.DecisionTreeClassifier() # MAX depth

dt.fit(x,y)
pred = []
# for i in range(len(y)):
#     print('gerçek değer: '+y[i])
#     pred.append(dt.predict(x[i].reshape(1,-1)))
#     print('tahmin sonucu: ' + dt.predict(x[i].reshape(1,-1)))
#     print('-'*20)

# print(np.array(y[:200]))
# print(np.array(pred))
# print(type(y))

