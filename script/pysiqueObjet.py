from .dicoDynamique import *
from .explosion import Explosion
from .base import Base
from .dico import *
import time

class ObjetPhysique(Base):
    def __init__(self,obj,x,y,nbExplosion,imgExplosion):
        Base.__init__(self,obj,x,y)
        self.obj = obj
        self.nbExplosion = nbExplosion
        self.imgExplosion = imgExplosion

        self.explosions = []
        self.moteur.canvas.coords(self.obj,self.x, self.y)
        for i in range(0,self.nbExplosion):
            self.explosions.append(Explosion(self.imgExplosion))
        

    def startExplosion(self):
        self.fireMove = False
        self.y_speed = 0
        self.x_speed = 0
        self.moteur.canvas.coords(self.obj,self.x, self.y)
        D_AUDIO['explosion'].play()
        # self.moteur.canvas.delete("all") 
        for u in range(0,self.nbExplosion):
            self.explosions[u].fire(self.position[0],self.position[1]) 


