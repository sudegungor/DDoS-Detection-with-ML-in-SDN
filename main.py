import numpy as np

from degerlendirme.degerlendirme import Degerlendirme
from egitilmis_modeller.egitilmis_model_controller import EgitilmisModelController

test2 = np.array(
    [
        # aşağıdaki veriler sudenin yakaladığı paket bilgileridir.
        # [0, 1, 0, 2, 54, 0],
        # [0, 1, 0, 0, 217, 2032],
        # burdan aşağısı eğitim görmemiş veri setinden alınmıştır
        [1, 0, 0, 0, 1032, 0],
        [1, 0, 0, 0, 1032, 0],
        [0, 0, 1, 4729, 147, 105],
        [1, 0, 0, 0, 520, 0],
        [0, 1, 0, 0, 207, 771],
    ]
)

controller = EgitilmisModelController()
scaler = controller.getStandardScaler()
decision = controller.getDecisionTreeClassifier()

degerlendirme = Degerlendirme()

test2 = scaler.transform(test2)



degerlendirme.test_et(
    test2,
    decision,
)


