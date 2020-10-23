from .dicoDynamique import *
from .explosion import Explosion
from .dico import *
import time

class Physique:
    def __init__(self,obj,x,y,nbExplosion,imgExplosion):
        self.obj
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.vitesseMax = 0
        self.time = 0
        self.angle = 0
        self.timeFire = 0
        self.fireMove = False
        self.fireOut = False

        self.nbExplosion = nbExplosion
        self.imgExplosion = imgExplosion

        self.position = []
        self.explosions = []
        self.moteur.canvas.coords(self.obj,self.x, self.y)
        for i in range(0,self.nbExplosion):
            self.explosions.append(Explosion(self.imgExplosion))
        self.moteur.canvas.pack()

        self.refresh()

    def refresh(self):
        if get_Pause() == False:
            self.time = time.time()
            self.position = self.moteur.canvas.coords(self.obj)
            self.fireColision()
            self.moteur.canvas.move(self.obj,self.x_speed,self.y_speed)
        self.moteur.fenetre.after(20,self.refresh)

    def miseAfire(self):
        self.fireMove = False
        self.y_speed = 0
        self.x_speed = 0
        self.moteur.canvas.coords(self.obj,self.x, self.y)
        D_AUDIO['explosion'].play()
        # self.moteur.canvas.delete("all") 
        for u in range(0,self.nbExplosion):
            self.explosions[u].fire(self.position[0],self.position[1]) 


    def refreshObj(self):
        pass

    def fireColision(self):
        pass
