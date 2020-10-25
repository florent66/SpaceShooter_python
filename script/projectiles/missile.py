from PIL import ImageTk 
from PIL import Image 
from PIL import ImageFilter
import random

from ..base import Base
from ..pysiqueObjet import ObjetPhysique
from ..dictionnaires.dicoDynamique import *
from ..dictionnaires.dico import *


class Missile(Base,ObjetPhysique):
    def __init__(self,D_OBJ_MISSILE_X):
        global nbExplosion
        self.moteur = get_Moteur()
        self.cage = D_OBJ_MISSILE_X['cage']
        self.D_OBJ_MISSILE_X = D_OBJ_MISSILE_X
        
        self.imgMissile = self.D_OBJ_MISSILE_X['image']
        self.imgMissile = self.imgMissile.resize((self.cage[0], self.cage[1]))
        self.tkimage = ImageTk.PhotoImage(self.imgMissile) 
        self.obj = self.moteur.canvas.create_image(0,0,anchor='nw', image=self.tkimage)
        # self.moteur.canvas.create_rectangle(self.x-50, self.y-50, self.x+50, self.y+50,fill='red')
        Base.__init__(self,self.obj,-100,550)
        ObjetPhysique.__init__(self,self.D_OBJ_MISSILE_X)
     

    def fire(self,x,y) :
        self.fireMove = True
        self.moteur.canvas.coords(self.obj,x,y)
        self.y_speed = -self.D_OBJ_MISSILE_X['speed']

    def colision(self):
        AjoutcolisionMissile(self,self.position,self.cage)
        if self.position[1] < 0:
            self.fireMove = False
            self.y_speed = 0
            self.moteur.canvas.coords(self.obj,self.x, self.y)        


