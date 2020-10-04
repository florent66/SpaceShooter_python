from PIL import ImageTk  
from PIL import Image 
from PIL import ImageFilter
import random
from .explosion import Explosion
from .moteurColision import dicoSon
import time
##test premier commit

class Decor:
    def __init__(self,moteur):
        self.moteur = moteur

        self.cage = [800,1333]
        self.x = 0
        self.y = -800
        self.x_speed = 0
        self.y_speed = 0
        self.imgDecor = Image.open("assets/images/decor.jpg") 
        #self.moteur.canvas.create_rectangle(self.x, self.y, self.x+self.cage[0], self.y+self.cage[1],fill='red')
        self.imgDecor = self.imgDecor.resize((self.cage[0],self.cage[1]))
        self.tkimage = ImageTk.PhotoImage(self.imgDecor) 
        self.objDecor = moteur.canvas.create_image(0,0,anchor='nw', image=self.tkimage)
        self.moteur.canvas.coords(self.objDecor,self.x, self.y)
        
        self.moteur.canvas.pack()

        self.physique()


    def physique(self):
        self.position = self.moteur.canvas.coords(self.objDecor)
        self.moteur.canvas.move(self.objDecor,0,0.2)
        self.moteur.fenetre.after(20,self.physique)