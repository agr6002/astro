from graphics import GraphWin, Point, Image
from asteroid import Asteroid
from datetime import datetime
from random import uniform, choice

class App:
    def __init__(self):
        print("Constructing App")
        self.win = GraphWin("ASTRO", 1024, 700)
        self.asteroidsImg = ["asteroid.png", "asteroid-big.png", "asteroid-small.png"]
        self.asteroids = []
        for i in range(5):
            self.asteroids.append(Asteroid(
                Image(Point(512, 384), choice(self.asteroidsImg)),
                uniform(-0.2, 0.2),
                uniform(-0.2, 0.2),
                self.win
            ))

    def launch(self):
        self.run()
    def run(self):
        epoch = datetime.utcfromtimestamp(0)
        timePrior = (datetime.now() - epoch).total_seconds() * 1000.0
        self.isRunning = True
        while (self.isRunning):
            timeNow = (datetime.now() - epoch).total_seconds() * 1000.0
            timeChange = timeNow - timePrior
            for i in range(5):
                self.asteroids[i].update(timeChange)
            timePrior = timeNow