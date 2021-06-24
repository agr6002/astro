from graphics import *
from random import uniform

class View:
    def __init__(self, vertShip, horShip, win):
        #print("  Constructing View")
        self.win = win
        self.ship = Image(Point(512, 384), "ship-small.png")
        self.vertShip = vertShip
        self.horShip = horShip

    def finalize(self):
        print("  finalizing View")    

    def initialize(self):
        print("  initializing View")
        self.ship.draw(self.win)

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
            print("shoot")

    def run(self, timeChange):
        self.setShipVel()
        self.ship.move(self.horShip * timeChange, self.vertShip * timeChange)
        #print(self.ship.anchor)

    def setVels(self, vertShip, horShip):
        self.vertShip = vertShip
        self.horShip = horShip