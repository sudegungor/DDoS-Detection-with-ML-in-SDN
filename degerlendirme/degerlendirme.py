import pickle
import os
import numpy as np

class Degerlendirme:

    def __init__(self):
        _path = os.path.abspath(
            os.path.join(os.path.dirname( __file__ ), '..', 'egitilmis_modeller')
        )
        
        self._label_encoder = pickle.load(
            open(f'{_path}/outcome_label_encoder', 'rb')
        )

    def test_et(self, test_verisi, siniflandirma_algoritmasi):
        sonuclar = siniflandirma_algoritmasi.predict(test_verisi)
        print('sınıfları:\n',self._label_encoder.inverse_transform(sonuclar.round().astype(int)))


_path = os.path.abspath(
            os.path.join(os.path.dirname( __file__ ), '..', 'egitilmis_modeller')
        )
        

test2 = np.array(
    [
     [0, 1, 0, 2, 54, 0],
     [0, 1, 0,0, 217, 2032]
    ]
)


decision = pickle.load(
    open(f'{_path}/decisionTreeClassifier', 'rb')
)

degerlendirme = Degerlendirme()

degerlendirme.test_et(
    test2,
    decision
)
