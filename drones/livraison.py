from 
class Livraison :

    def __init__(self, destination: str, priorite: int, poids_colis: float, statut: str = ""):
        """
        Classe qui contient l'info des livraisons
        """
        # En ne mettant pas la variable privée, j'appelle sa validation lors de l'initialisation (setter).
        self.destination = destination
        self.priorite = priorite
        self.poids_colis = poids_colis

