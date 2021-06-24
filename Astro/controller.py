class Controller:
    def __init__(self, vertShip, horShip, win):
        #print("  Constructing Controller")
        self.win = win
        self.vertShip = vertShip
        self.horShip = horShip

    def finalize(self):
        print("  finalizing Controller") 

    def initialize(self):
        print("  initializing Controller")

    def run(self):
        #print("  running Controller") 
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
            return