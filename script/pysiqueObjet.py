from PIL import ImageTk 
from PIL import Image 
from PIL import ImageFilter
import time
import random
from .dictionnaires.dico import *
from .dictionnaires.dicoDynamique import *
from .base import Base

class ObjetPhysique():
    def __init__(self,D_CONF_X):
        self.nbExplosion = D_CONF_X['nbExplosion']
        self.imgExplosion = D_CONF_X['imgExplosion']

        self.explosions = []
        # self.moteur.canvas.coords(self.obj,self.x, self.y)
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

    def blessure(self):
        self.fireMove = False
        self.y_speed = 0
        self.x_speed = 0
        self.moteur.canvas.coords(self.obj,self.x, self.y)
        D_AUDIO['explosion'].play()
        # self.moteur.canvas.delete("all") 
        for u in range(0,self.nbExplosion):
            self.explosions[u].fire(self.position[0],self.position[1]) 


class Explosion(Base):
    def __init__(self,image):
        self.moteur = get_Moteur()
        self.x = -100
        self.y = 500
        self.imgExplosion= Image.open(image) 
        self.imgExplosion = self.imgExplosion.resize((int(random.uniform(2,10)),int(random.uniform(2,10))))
        self.tkimage = ImageTk.PhotoImage(self.imgExplosion) 
        self.obj= self.moteur.canvas.create_image(0,0,anchor='nw', image=self.tkimage)
        Base.__init__(self,self.obj,self.x,self.y)
        self.moteur.canvas.pack()
    

    def fire(self,x,y) :
        self.moteur.canvas.coords(self.obj,x,y)
        self.x_speed = random.uniform(-5,5) 
        self.y_speed = random.uniform(1,-6) 