from PIL import ImageTk  
from PIL import Image 
from PIL import ImageFilter
import random
from .explosion import Explosion
from .pysiqueObjet import Physique
from .dicoDynamique import *
from .dico  import *

# from tkMessageBox import *
# from Tkinter import * 
##test premier commit

class Panda(Physique):
    def __init__(self,x,y,cage):
        self.moteur = get_Moteur()
        self.cage = cage

        
        self.imgPandaOrigine = D_IMAGE['panda']
        self.spritePanda = []
        #self.moteur.canvas.create_rectangle(self.x, self.y, self.x+self.cage[0], self.y+self.cage[1],fill='red')
        for i in range(0,360):
            self.imgPanda = self.imgPandaOrigine.resize((self.cage[0],self.cage[1]))
            self.imgPanda = self.imgPanda.rotate(i)
            self.tkimage = ImageTk.PhotoImage(self.imgPanda)
            self.spritePanda.append(self.tkimage)
 
        self.obj = self.moteur.canvas.create_image(0,0,anchor='nw', image=self.spritePanda[0])
     
        #self.moteur.canvas.itemconfigure(self.obj, state="hidden") #pour agir sur les options ici idden ou "normal"
        Physique.__init__(self,self.obj,x,y,5,"assets/images/panda.png")


    def fireColision(self):
        AjoutcolisionPanda(self,self.position,self.cage)
        deltaTime = self.time - self.timeFire 
        
        # if deltaTime > 0.01:
        self.angle += 4
        if self.angle > 359:
            self.angle = 0

        self.moteur.canvas.itemconfigure(self.obj,image=self.spritePanda[self.angle]) 


