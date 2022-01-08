import numpy as np

from degerlendirme.degerlendirme import Degerlendirme
from egitilmis_modeller.egitilmis_model_controller import EgitilmisModelController
import sys
import os

def okunanVeridenSonuca(res):
    encoded_protocol_type = ohe.transform(np.array([res['protocol_type']]).reshape((-1, 1))).toarray()[0].astype(int)
    test = encoded_protocol_type
    test = np.append(test, res['duration'])
    test = np.append(test, int(str(res['destination_ip']).replace('.', '')))
    test = np.append(test, int(str(res['source_ip']).replace('.', '')))
    print(test)
    degerlendirme.test_et(
        [test],
        classifier,
    )


from terminal_controller.terminal import Terminal
test2 = np.array(
    [
        # aşağıdaki veriler sudenin yakaladığı paket bilgileridir.
        # [0, 1, 0, 2, 54, 0],
        # [0, 1, 0, 0, 217, 2032],
        # burdan aşağısı eğitim görmemiş veri setinden alınmıştır
        [1, 0, 0, 0, 1032, 0], # gerçek değer ddos
        [1, 0, 0, 0, 1032, 0], # gerçek değer ddos
        [0, 0, 1, 4729, 147, 105], # gerçek değer normal
        [1, 0, 0, 0, 520, 0], # gerçek değer ddos
        [0, 1, 0, 0, 207, 771], # gerçek değer normal
    ]
)

controller = EgitilmisModelController()
scaler = controller.getStandardScaler()
classifier = controller.getYSAModel()
ohe = controller.getProtocolTypeOneHotEncoder()

degerlendirme = Degerlendirme()

test2 = scaler.transform(test2)

# script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'deneme', 'parent.py'))
# print(script_path)
# res = Terminal.run([sys.executable, '-u', script_path])


# okunanVeridenSonuca(res)


degerlendirme.test_et(
    test2,
    classifier
 )


