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

    def __init__(self, identifiant: str, latitude: float, longitude: float) -> None:

        Drone._compteur_drones += 1

    @abstractmethod
    def consommation_batterie(self):
        pass
