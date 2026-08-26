# ABC : Abstract Base Classes
from abc import ABC, abstractmethod
from datetime import datetime
from random import uniform
from .livraison import Livraison

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
        self._batterie: float = 100.00
        Drone._compteur_drones += 1
        self._livraison_actuelle: Livraison = None
        self._batterie_max: float = self._batterie


    @property
    def identifiant(self):
        return self.identifiant

    @identifiant.setter
    def identifiant(self, identifiant: str):
        if identifiant == "":
            pass
        self.identifiant = identifiant

    @property
    def latitude(self):
        return self.latitude

    @latitude.setter
    def latitude(self, latitude: int):
        self.latitude = latitude

    @property
    def longitude(self):
        return self.longitude

    @longitude.setter
    def longitude(self, longitude: int):
        self.longitude = longitude

    @property
    def _batterie(self):
        return self._batterie

    @_batterie.setter
    def _batterie(self, _batterie: float):
        if _batterie < 0 | _batterie > self._batterie_max :
            pass
        self._batterie = _batterie

    @property
    def _livraison_actuelle(self):
        return self._livraison_actuelle

    @_livraison_actuelle.setter
    def _livraison_actuelle(self, livraison_actuelle: Livraison):
        self._livraison_actuelle = livraison_actuelle

    # La batterie max ne devrait pas changer
    @property
    def _batterie_max(self):
        return self._batterie_max

    
    @abstractmethod
    def consommation_batterie(self):
        pass
