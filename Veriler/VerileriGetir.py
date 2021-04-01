import pandas as pd
from sklearn.model_selection import train_test_split
veriler = pd.read_csv('Veriler/BakalımOlmusMu.csv')
Y = veriler['outcome']
X = veriler.drop(columns=['outcome'])

def verileriGetir():

    #işlemler numpy dizileri üzerinden işleyeceği için
    x = X.values
    y = Y.values
    return X,Y,x,y

def setiBol():
    return train_test_split(X, Y, test_size=0.33)
