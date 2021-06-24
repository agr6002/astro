class Asteroid:
    def __init__(self, img, velX, velY, win):
        print("  Constructing Asteroid")
        self.img = img
        self.dimX = img.getWidth()
        self.dimY = img.getHeight()
        self.posX = img.getAnchor().x
        self.posY = img.getAnchor().y
        self.velX = velX
        self.velY = velY
        self.win = win
        self.img.draw(self.win)

    def update(self, timeChange):
        print(self.dimX)
        print(self.dimY)
        dx = self.velX * timeChange
        dy = self.velY * timeChange
        self.posX += dx
        self.posY += dy
        if (self.posX > self.win.width + self.dimX / 2):
            self.posX -= (self.win.width + self.dimX)
            dx -= (self.win.width + self.dimX)
        elif (self.posX < -self.dimX / 2):
            self.posX += (self.win.width + self.dimX)
            dx += (self.win.width + self.dimX)
        if (self.posY > self.win.height + self.dimY / 2):
            self.posY -= (self.win.height + self.dimY)
            dy -= (self.win.height + self.dimY)
        elif (self.posY < -self.dimY / 2):
            self.posY += (self.win.height + self.dimY)
            dy += (self.win.height + self.dimY)
        self.img.move(dx, dy)
