if __name__ == "__main__":
    from drones import DroneLeger
    from drones import Drone

    dl: DroneLeger = DroneLeger(identifiant="23rT", latitude=0, longitude=0)
    print(dl._batterie)
    dl.consommer_batterie()
    print(dl.batterie)
