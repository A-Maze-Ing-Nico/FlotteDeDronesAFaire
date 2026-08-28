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

        # Je ne comprenais pas le concept de charge_max. Je croyais c'était en lien avec la recharge de la batterie, oops.

    @property
    def identifiant(self):
        return self._identifiant

    @identifiant.setter
    def identifiant(self, identifiant: str):
        if identifiant == "":
            pass
        self._identifiant = identifiant

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: int):
        self._latitude = latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: int):
        self._longitude = longitude

    @property
    def batterie(self):
        return self._batterie

    @batterie.setter
    def batterie(self, batterie: float):
        if batterie < 0 or batterie > self._batterie_max:
            pass
        self._batterie = batterie

    @property
    def livraison_actuelle(self):
        return self._livraison_actuelle

    @livraison_actuelle.setter
    def livraison_actuelle(self, livraison_actuelle: Livraison):
        self._livraison_actuelle = livraison_actuelle

    # La batterie max ne devrait pas changer
    @property
    def batterie_max(self):
        return self._batterie_max

    @abstractmethod
    def consommer_batterie(self) -> None:
        pass
