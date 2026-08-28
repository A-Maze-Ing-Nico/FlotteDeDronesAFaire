# Là où il y a des pass dans les classes, il devrait y avoir des raise error et ses erreurs devraient être gérées dans le

if __name__ == "__main__":
    from drones import DroneLeger
    from drones import DroneLourd
    from drones import Livraison

    dle: DroneLeger = DroneLeger(identifiant="23rT", latitude=0, longitude=0)
    print(dle.batterie)
    dle.consommer_batterie()
    print(dle.batterie)

    dlo = DroneLourd(identifiant="23rT", latitude=0, longitude=0)
    dlo.consommer_batterie()
    print(dlo.batterie)

    livraison = Livraison(destination="G-town", priorite=2, poids_colis=2.9)

    dlo.livraison_actuelle = livraison
    dlo.consommer_batterie()
    print(dlo.batterie)
