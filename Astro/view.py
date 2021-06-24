from graphics import *
from asteroid import Asteroid
from lazer import Lazer
from random import uniform, choice, random
from math import sqrt

class View:
    def __init__(self, vertShip, horShip, lazers, win):
        #print("  Constructing View")
        self.win = win
        self.asteroidsImg = ["asteroid.png", "asteroidBig.png", "asteroidBig.png", "asteroidSmall.png"]
        self.astroH = 200
        self.astroBigH = 300
        self.astroSmallH = 100
        self.ship = Image(Point(512, 384), "shipSmall.png")
        self.vertShip = vertShip
        self.horShip = horShip
        self.asteroids = []
        self.lazers = lazers

    def finalize(self):
        print("  finalizing View")
        End = Text(Point(512, 384), "Game Over")
        End.draw(self.win)   

    def initialize(self):
        print("  initializing View")
        for i in range(5):
            self.asteroids.append(Asteroid(
                Image(Point(512, 384), choice(self.asteroidsImg)),
                uniform(0.1, 0.5) * self.signX(),
                uniform(0.1, 0.5) * self.signY(),
                self.win
            ))
        self.ship.draw(self.win)

    def signX(self):
            rX = random()
            if rX < 0.5:
                return -1
            else:
                return 1
    
    def signY(self):
        rY = random()
        if rY < 0.5:
            return -1
        else:
            return 1

    def setShipVel(self):
        press = self.win.checkKey()
        change = 0.7
        self.vertShip = 0
        self.horShip = 0
        if(press == "s"):
            self.vertShip = change
        elif(press == "w"):
            self.vertShip = -change
        elif(press == "d"):
            self.horShip = change
        elif(press == "a"):
            self.horShip = -change
        elif(press == "space"):
            self.lazers.append(Lazer(
                self.ship, 
                0, #uniform(-0.2, 0.2),
                -0.2, #uniform(-0.2, -0.1), 
                self.win))
 
    def run(self, timeChange):
        #print("  running View")

        for i in range(len(self.asteroids)):
            self.asteroids[i].update(timeChange)
            #print(str(i))
        self.setShipVel()
        self.ship.move(self.horShip * timeChange, self.vertShip * timeChange)
        #print(self.ship.anchor)
        ae = -1
        for e in range(len(self.lazers)):
            ae += 1
            if(self.lazers[ae].update(timeChange) == False):
                self.lazers.pop(ae)
                ae -= 1
        
        asa = -1
        for a in range(len(self.asteroids)):
            asa += 1
            astro = self.asteroids[asa]
            if(len(self.asteroids) == 0):
                self.finalize
            lsa = -1
            for l in range(len(self.lazers)):
                lsa += 1
                lazer = self.lazers[lsa]
                dx = lazer.lazer.getCenter().x - astro.posX
                dy = lazer.lazer.getCenter().y - astro.posY
                d = sqrt(dx * dx + dy * dy)
                if (d < astro.dimX/2):
                    self.lazers[lsa].undraw()
                    self.lazers.pop(lsa)
                    lsa -= 1
                    if(self.asteroids[asa].img.getHeight() > self.astroH):
                        for i in range(3):
                            self.asteroids.append(Asteroid(
                                Image(self.asteroids[asa].img.getAnchor(), "asteroid.png"),
                                uniform(0.1, 0.3) * self.signX(),
                                uniform(0.1, 0.3) * self.signY(),
                                self.win
                            ))
                    elif(self.asteroids[asa].img.getHeight() > self.astroSmallH ):
                        for i in range(2):
                            self.asteroids.append(Asteroid(
                                Image(self.asteroids[asa].img.getAnchor(), "asteroidSmall.png"),
                                uniform(0.1, 0.3) * self.signX(),
                                uniform(0.1, 0.3) * self.signY(),
                                self.win
                            ))
                    else:
                        print("none")
                    self.asteroids[asa].undraw()
                    self.asteroids.pop(asa)
                    asa -= 1
                    if(len(self.asteroids) == 0):
                        self.finalize
    def setVelsLaz(self, vertShip, horShip, lazers):
        self.vertShip = vertShip
        self.horShip = horShip
        self.lazers = lazers
