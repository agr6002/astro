from graphics import *

class Lazer:
    def __init__(self, ship, velX, velY, win):
        self.ship = ship
        self.length = 14
        self.posX1 = self.ship.getAnchor().x
        self.posY1 = self.ship.getAnchor().y - self.ship.getHeight()/2
        self.posX2 = self.posX1
        self.posY2 = self.posY1 + self.length
        self.lazer = Line(Point(self.posX1, self.posY1), Point(self.posX2, self.posY2))
        self.velX = velX
        self.velY = velY
        self.win = win
        self.lazer.setOutline("red")
        self.lazer.setWidth(2.5)
        self.lazer.draw(self.win)

    def update(self, timeChange):
        if(
            (
                (self.posX1 or self.posX2) < 0 
                or 
                (self.posX1 or self.posX2) > self.win.width
            )
            or
            (
                (self.posY1 or self.posY2) < 0 
                or 
                (self.posY1 or self.posY2) > self.win.height
            )    
        ):
            self.lazer.undraw()
            return False
        dx = self.velX * timeChange
        dy = self.velY * timeChange
        self.posX1 += dx
        self.posY1 += dy
        self.posX2 += dx
        self.posY2 += dy
        self.lazer.move(dx, dy)

    def undraw(self):
        self.lazer.undraw()