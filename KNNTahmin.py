from sklearn.neighbors import KNeighborsClassifier
from Veriler.VerileriGetir import setiBol
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, plot_confusion_matrix


X_train, X_test, y_train, y_test = setiBol()


knn = KNeighborsClassifier() # n_neighbors=5 --> varsayılan değer

knn.fit(X_train,y_train)

pred = knn.predict(X_test)
cm = confusion_matrix(pred, y_test)
print(cm)

#confusion matrisini (doğruluk matrisini göstermek için kullanıyorum)
plot_confusion_matrix(knn, X_test, y_test)
plt.show()


# plt.plot(pred,y_test , '.g')
# plt.show()


