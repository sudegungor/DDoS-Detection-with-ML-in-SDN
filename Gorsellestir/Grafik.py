import matplotlib.pyplot as plt


def veriyiGorsellestir(y_gercek,y_tahmin):
    plt.plot(y_gercek,y_tahmin, 'r.')
    plt.xticks(rotation=30)
    plt.show()

