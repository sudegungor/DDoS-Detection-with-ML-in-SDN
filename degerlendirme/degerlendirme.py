import numpy as np
from egitilmis_modeller.egitilmis_model_controller import EgitilmisModelController


class Degerlendirme:

    def __init__(self):
        __egitilmisModelController = EgitilmisModelController()
        self.__label_encoder = __egitilmisModelController.getOutcomeLabelEncoder()

    def test_et(self, test_verisi, siniflandirma_algoritmasi, gercek_degerler = None):
        sonuclar = siniflandirma_algoritmasi.predict(test_verisi)
        if (gercek_degerler is not None):
            for (sonuc, gercek_deger) in (sonuclar, gercek_degerler):
                sonuc_adi = self.__label_encoder.inverse_transform([sonuc])[0]
                gercek_deger_adi = self.__label_encoder.inverse_transform([gercek_deger])[0]
                print(f'tahmin edilen sonuç: {sonuc_adi} gerçek değer {gercek_deger_adi}')
        else:
            for sonuc in sonuclar:
                sonuc_adi = self.__label_encoder.inverse_transform([sonuc.round().astype(int)])[0]
                print(f'tahmin edilen sonuç: {sonuc_adi}')
