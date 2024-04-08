class Band:
    def __init__(self, band_name=""):
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Musician."""
        musician_info = []
        for musician in self.musicians:
            musician_info.append(f"{musician.name} ({musician.instruments})")
        return f"{self.band_name} ({', '. join(musician_info)})"

    def __repr__(self):
        """Return a string representation of a Musician, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        play_str = ""
        for musician in self.musicians:
            if not musician.instruments:
                play_str += f"{musician.name} needs an instrument!\n"
            else:
                play_str += f"{musician.name} is playing: {musician.instruments[0]}\n"
        return play_str
