from .drone import Drone
from .statut_drone import StatutDrone

# Éléments publics qu'on veut exposer depuis ce package (drones)
# N'empêche pas les classes non mentionnées d'être exposées
__all__ = ["Drone", "StatutDrone"]
