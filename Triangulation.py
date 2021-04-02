import matplotlib.pyplot as plt

VITESSTE_ONDES_P = 6e3  # 6 km par secondes
VITESSTE_ONDES_S = 4.06e3  # 4.06 km par secondes

fig, ax = plt.subplots()  # note we must use plt.subplots, not plt.subplot
ax.axis("equal")  # Axes de même longueur
ax.set_xlim(-100e3, 200e3)  # Axes des abscisses
ax.set_ylim(-100e3, 200e3)  # Axes des ordonnées


class Station():
    """
    Station découte sismique ou autre récepteur d'onde
    """
    stations = []

    def __init__(self, coordonnées, name):
        self.coordonnées = coordonnées  # Coordonnées de la station (x, y)
        self.name = name  # Nom de la station
        self.rayon = 0  # Rayon du cercle
        # Draw the point of the station
        plt.scatter(self.coordonnées[0], self.coordonnées[1], label=self.name)
        Station.stations.append(self)

    def drawCircleEpicentreByDifferencePandSWaves(self, retard):
        self.rayon = retard * ((VITESSTE_ONDES_P*VITESSTE_ONDES_S) /
                               (VITESSTE_ONDES_P-VITESSTE_ONDES_S))  # On calcule le rayon
        self.circle = plt.Circle(
            self.coordonnées, self.rayon, fill=False, ec="red", lw=1)  # Circle
        ax.add_artist(self.circle)  # Ajoute cercle

    def __repr__(self):
        return "SATION NAME : " + self.name + "\n" + "RAYON : " + str(round(self.rayon/1000, 3))+" km"


sta1 = Station((20e3, 20e3), "STA1")
sta1.drawCircleEpicentreByDifferencePandSWaves(3)
print(sta1)
sta2 = Station((100e3, 20e3), "STA2")
sta2.drawCircleEpicentreByDifferencePandSWaves(5)
print(sta2)
sta3 = Station((150e3, -10e3), "STA3")
sta3.drawCircleEpicentreByDifferencePandSWaves(8.43)
print(sta3)


plt.legend(loc="best")  # Légende
plt.title("Triangulation")  # Title
plt.grid(linestyle="-")
plt.show()  # Affiche
