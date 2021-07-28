from abc import ABC


class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums")

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar")

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass")

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Band:

    bands = []

    def __init__(self, name, members):
        self.members = members
        self.name = name
        Band.bands.append(self.name)

    def __str__(self):
        return f"The band {self.name}"

    @classmethod
    def to_list(cls):
        return cls.bands

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos
