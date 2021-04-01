from sklearn import tree
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from Veriler import VerileriGetir
X,Y,x,y = VerileriGetir.verileriGetir()

dt = tree.DecisionTreeClassifier() # MAX depth

dt.fit(x,y)
pred = []
for i in range(len(y)):
    print('gerçek değer: '+y[i])
    pred.append(dt.predict(x[i].reshape(1,-1)))
    print('tahmin sonucu: ' + dt.predict(x[i].reshape(1,-1)))
    print('-'*20)

# print(np.array(y[:200]))
# print(np.array(pred))
# print(type(y))

