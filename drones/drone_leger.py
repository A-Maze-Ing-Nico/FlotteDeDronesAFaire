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
        #Il manque un getter et setter
        self._consommation_batterie = consommation_batterie

    def consommer_batterie(self) -> None:
        self._batterie -= self._consommation_batterie