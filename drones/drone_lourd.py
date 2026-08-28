from .drone import Drone


class DroneLourd(Drone):
    def __init__(
        self,
        identifiant: str,
        latitude: float,
        longitude: float,
        consommation_batterie: float = 10,
    ):
        super().__init__(identifiant, latitude, longitude)
        # Il manque un getter et setter
        self.consommation_batterie = consommation_batterie

    def consommer_batterie(self):
        if self._livraison_actuelle != None:
            self._batterie -= (
                self._livraison_actuelle.poids_colis * self.consommation_batterie
            )
            if self._batterie < 0:
                self._batterie = 0
        else:
            pass
