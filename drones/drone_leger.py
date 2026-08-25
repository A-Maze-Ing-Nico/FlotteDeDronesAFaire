from .drone import Drone


class DroneLeger(Drone):
    def __init__(
        self,
        identifiant: str,
        latitude: float,
        longitude: float,
        consommation_batterie: float = 5,
    ):
        super().__init__(identifiant, latitude, longitude)

        self.consommation_batterie = consommation_batterie
