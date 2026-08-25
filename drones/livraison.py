from .statut_livraison import StatutLivraison


class Livraison:
    def __init__(self, destination: str, priorite: int, poids_colis: float):
        """
        Classe qui contient l'info des livraisons
        """
        # En ne mettant pas la variable privée, j'appelle sa validation lors de l'initialisation (setter).
        self.destination = destination
        self.priorite = priorite
        self.poids_colis = poids_colis
        self._statut = StatutLivraison.EN_COURS

        @property
        def destination(self):
            return self.destination

        @destination.setter
        def destination(self, destination: str):
            if destination == "":
                pass
            self.destination = destination

        @property
        def priorite(self):
            return self.priorite

        @priorite.setter
        def priorite(self, priorite: int):
            if priorite <= 0 | priorite > 10:
                pass
            self.priorite = priorite

        @property
        def poids_colis(self):
            return self.poids_colis

        @poids_colis.setter
        def poids_colis(self, poids_colis: float):
            if poids_colis <= 0:
                pass
            self.poids_colis = poids_colis

        # Si un attribut est privé, devrait-on mettre un getter???
        @property
        def statut(self):
            return self._statut

        # C'est weird ici le self qui s'est ajouté...
        @self._statut.setter
        def _statut(self, statut: StatutLivraison):
            self._statut = statut
