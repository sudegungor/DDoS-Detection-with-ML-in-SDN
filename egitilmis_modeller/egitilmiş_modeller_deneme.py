import pickle
import os

class EgitilmisModelController:

    def __init__(self):
        self.__path = os.path.abspath(
            os.path.dirname( __file__ )
        )

    def __loadClasses(self, name):
        loadedClass = pickle.load(
            open(f'{self.__path}/{name}', 'rb')
        )
        return loadedClass

    def getDecisionTreeClassifier(self):
        
        return self.__loadClasses('decisionTreeClassifier')

    def getNaiveBayesClassifier(self):
        return self.__loadClasses('naiveBayes')


    def getStandardScaler(self):
        return self.__loadClasses('standard_scaler')

    def getOutcomeLabelEncoder(self):
            return self.__loadClasses('outcome_label_encoder')



controller = EgitilmisModelController()

encoder = controller.getOutcomeLabelEncoder()

res = encoder.inverse_transform([1, 0])

print(res)