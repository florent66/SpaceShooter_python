from PIL import ImageTk  
from PIL import Image 
from PIL import ImageFilter
import math
import random
from ..base import Base
from ..explosionPhysique import ExplosionPhysique
from ..dictionnaires.dicoDynamique import *
from ..dictionnaires.dico  import *

# from tkMessageBox import *
# from Tkinter import * 
##test premier commit

class Panda(Base,ExplosionPhysique):
    def __init__(self,x,y,cage):
        self.moteur = get_Moteur()
        self.cage = cage

        
        self.imgPandaOrigine = D_CONF_PANDA['image']
        self.spritePanda = []
        #self.moteur.canvas.create_rectangle(self.x, self.y, self.x+self.cage[0], self.y+self.cage[1],fill='red')
        for i in range(0,359):
            self.imgPanda = self.imgPandaOrigine.resize((self.cage[0],self.cage[1]))
            self.imgPanda = self.imgPanda.rotate(i)
            self.tkimage = ImageTk.PhotoImage(self.imgPanda)
            self.spritePanda.append(self.tkimage)
 
        self.obj = self.moteur.canvas.create_image(0,0,anchor='nw', image=self.spritePanda[0])
     
        #self.moteur.canvas.itemconfigure(self.obj, state="hidden") #pour agir sur les options ici idden ou "normal"
        Base.__init__(self,self.obj,x,y,D_CONF_PANDA)
        ExplosionPhysique.__init__(self,D_CONF_PANDA)

    def colision(self):
        AjoutcolisionPanda(self,self.position,self.cage)
        deltaTime = self.time - self.timeFire 
        self.angle = 10
        # if deltaTime > 0.01:
        #rotation automatique vers vaisseau
        # self.angle += 4
        # if self.angle > 359:
        #     self.angle = 0
        try:

            
            tang = (self.position[1] - self.moteur.vaisseau.position[1])/(self.position[0] - self.moteur.vaisseau.position[0])
            self.angle = -round(math.degrees(math.atan(tang)))
            if (self.moteur.vaisseau.position[0] < self.position[0]):
                self.angle += 180

            # print(self.angle)
        except:
            pass
      

        self.moteur.canvas.itemconfigure(self.obj,image=self.spritePanda[self.angle]) 


