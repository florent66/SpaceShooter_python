from .dicoDynamique import *
from .dico import *
import time

class Base:
    def __init__(self,obj,x,y):
        self.obj = obj
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.x_acc = 0
        self.y_acc = 0
        self.vitesseMax = 0
        self.time = 0
        self.angle = 0
        self.timeFire = 0
        self.fireMove = False
        self.fireOut = False
        self.position = [0,0]
        self.moteur.canvas.coords(self.obj,self.x, self.y)
        self.moteur.canvas.pack()
        self.refresh()

    def refresh(self):
        if get_Pause() == False:
            self.time = time.time()
            self.position = self.moteur.canvas.coords(self.obj)
            self.fireColision()
            self.moteur.canvas.move(self.obj,self.x_speed,self.y_speed)
            self.refreshObj()
        self.moteur.fenetre.after(20,self.refresh)


    def refreshObj(self):
        pass

    def fireColision(self):
        pass
