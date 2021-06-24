from model import Model
from view import View
from controller import Controller
from datetime import datetime
from graphics import GraphWin

class App:
    def __init__(self):
        print("Constructing App")
        self.win = GraphWin("ASTRO", 1024, 700)
        self.vertShip = 0
        self.horShip = 0
        self.lazers = []
        self.model = Model()
        self.view = View(self.vertShip, self.horShip, self.lazers, self.win)
        self.controller = Controller(self.vertShip, self.horShip, self.win)
        self.isRunning = False
        self.launch()
        
    def finalize(self):
        print("finalizing App")
        #self.model.finalize()
        #self.controller.finalize() 
        self.view.finalize()

    def initialize(self):
        print("initializing App")
        #self.model.initialize()
        #self.controller.initialize()
        self.view.initialize()        

    def launch(self):
        self.initialize()
        self.run()
        self.finalize()

    def run(self):
        print("running App")
        epoch = datetime.utcfromtimestamp(0)
        timePrior = (datetime.now() - epoch).total_seconds() * 1000.0
        self.isRunning = True
        while (self.isRunning):
            timeNow = (datetime.now() - epoch).total_seconds() * 1000.0
            timeChange = timeNow - timePrior
            #self.controller.run() 
            #print(str(self.horShip) + " " + str(self.vertShip))         
            #self.model.run()
            #self.view.setVelsLaz(self.vertShip, self.horShip, self.lazers)
            self.view.run(timeChange)
            timePrior = timeNow