# ABC : Abstract Base Classes
from abc import ABC, abstractmethod
from datetime import datetime
from random import uniform

from .statut_drone import StatutDrone


class Drone(ABC):
    """
    Classe de base pour tous les types de drônes
    """

    # Attributs de classe (directement dans le corps de la classe et pas dans le init)
    #   ==> Partagé par toutes les instances.
    _compteur_drones: int = 0

    # Malheureusement, les méthodes statiques ne peuvent pas modifier les variables statiques. C'est dum >:(
    # @staticmethod
    # def incrementer_compteur_drones(nombre_a_ajouter: int) -> None:
    #     _compteur_drones += nombre_a_ajouter 

    def __init__(self, identifiant: str, latitude: float, longitude: float) -> None:
        self.identifiant = identifiant
        self.latitude = latitude
        self.longitude = longitude
        self._batterie = 100.00
        Drone._compteur_drones += 1

    @abstractmethod
    def consommation_batterie(self):
        pass
