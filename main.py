if __name__ == "__main__":
    from drones import DroneLeger

    dl: DroneLeger = DroneLeger(identifiant="23rT", latitude=0, longitude=0)
    print(dl.batterie)
    dl.consommer_batterie()
    print(dl.batterie)
