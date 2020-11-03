from PIL import ImageTk 
from PIL import Image 
from PIL import ImageFilter
import time
import random
from .dictionnaires.dico import *
from .dictionnaires.dicoDynamique import *
from .base import Base

class ExplosionPhysique():
    def __init__(self,D_CONF_X):
        self.nbExplosion = D_CONF_X['nbExplosion']
        self.imgExplosion = D_CONF_X['imgExplosion']

        self.explosions = []
        # self.moteur.canvas.coords(self.obj,self.x, self.y)
        for i in range(0,self.nbExplosion):
            self.explosions.append(Explosion(self.imgExplosion))


    def startExplosion(self):

        # self.moteur.canvas.delete("all")
        self.vie = self.vie - 2
        if (self.vie <= 0):
            self.vie = self.D_OBJ_X['vie']
            self.fireMove = False
            self.y_speed = 0
            self.x_speed = 0

            ##Si explosion on passe à l 'animation de l 'entité suivante voir conf ..
            ##Si il n'y a plus d 'animation c 'est le repos
            if (self.lenAnimation  > self.indexAnimation):
                 self.indexAnimation += 1
                 self.moteur.canvas.coords(self.obj,self.numAnimation[str(self.indexAnimation)][0], self.numAnimation[str(self.indexAnimation)][1])
            else:
                self.moteur.canvas.coords(self.obj,self.numAnimation['repos'][0], self.numAnimation['repos'][1])

            D_AUDIO['explosion'].play()
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
        Base.__init__(self,self.obj,self.x,self.y,D_OBJ_EXPLOSION)
        self.moteur.canvas.pack()
    

    def fire(self,x,y) :
        self.moteur.canvas.coords(self.obj,x,y)
        self.x_speed = random.uniform(-5,5) 
        self.y_speed = random.uniform(1,-6) 