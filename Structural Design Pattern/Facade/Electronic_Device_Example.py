class DVD:
    def on(self):
        print("DVD player On")

    def play(self, movie):
        print(f'Play movie {movie}')

    def off(self):
        print("DVD player Off")


class Amplifier:
    def on(self):
        print("Amplifier On")

    def off(self):
        print("Amplifier Off")  # corrected

    def play(self, volume):
        print(f'Amplifier set volume {volume}')


class Projector:
    def on(self):
        print("Projector On")

    def off(self):
        print("Projector Off")  # corrected

    def projector_mode(self, mode):
        print(f'Projector {mode} mode is on')


class HomeTheater:
    def __init__(self):
        # create object instances
        self.dvd = DVD()
        self.amplifier = Amplifier()
        self.projector = Projector()

    def play_movie(self, movie):
        print("\n--- Starting Home Theater ---")
        self.dvd.on()
        self.amplifier.on()
        self.projector.on()
        self.dvd.play(movie)
        self.amplifier.play(7)
        self.projector.projector_mode("dark")

    def off_movie(self):
        print("\n--- Shutting Down Home Theater ---")
        self.dvd.off()
        self.amplifier.off()
        self.projector.off()


# Example usage
home = HomeTheater()
home.play_movie("Inception")
home.off_movie()
