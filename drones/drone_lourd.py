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

        self.consommation_batterie = consommation_batterie

    def consommation_batterie(self):
        pass