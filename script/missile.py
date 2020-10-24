from PIL import ImageTk 
from PIL import Image 
from PIL import ImageFilter
import random

from .pysiqueObjet import ObjetPhysique
from .dicoDynamique import *
from .dico import *




class Missile(ObjetPhysique):
    def __init__(self):
        global nbExplosion
        self.moteur = get_Moteur()
        self.cage = [20,20]
        
        self.imgMissile = Image.open("assets/images/missile.png") 
        self.imgMissile = self.imgMissile.resize((self.cage[0], self.cage[1]))
        self.tkimage = ImageTk.PhotoImage(self.imgMissile) 
        self.obj = self.moteur.canvas.create_image(0,0,anchor='nw', image=self.tkimage)
        # self.moteur.canvas.create_rectangle(self.x-50, self.y-50, self.x+50, self.y+50,fill='red')
        
        ObjetPhysique.__init__(self,self.obj,-100,550,D_CONF_MISSILE['nbEplosion'],"assets/images/explosion.png")
     

    def fire(self,x,y) :
        self.fireMove = True
        self.moteur.canvas.coords(self.obj,x,y)
        self.y_speed = -15

    def fireColision(self):
        AjoutcolisionMissile(self,self.position,self.cage)
        if self.position[1] < 0:
            self.fireMove = False
            self.y_speed = 0
            self.moteur.canvas.coords(self.obj,self.x, self.y)        


