from PIL import ImageTk  
from PIL import Image 
from PIL import ImageFilter
import random
from .explosion import Explosion
from .moteurColision import AjoutcolisionPanda
from .moteurColision import dicoSon
import time
##test premier commit

class Panda:
    def __init__(self,moteur,x,y):
        self.moteur = moteur

        self.cage = [30,30]
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.imgPanda = Image.open("assets/images/panda.png") 
        #self.moteur.canvas.create_rectangle(self.x, self.y, self.x+self.cage[0], self.y+self.cage[1],fill='red')
        self.imgPanda = self.imgPanda.resize((self.cage[0],self.cage[1]))
        self.tkimage = ImageTk.PhotoImage(self.imgPanda) 
        self.objPanda = moteur.canvas.create_image(0,0,anchor='nw', image=self.tkimage)
        self.moteur.canvas.coords(self.objPanda,self.x, self.y)
        
        self.moteur.canvas.pack()
        self.position = []
        self.explosions = []
        self.nbExplosion = 5

        for i in range(0,self.nbExplosion):
            self.explosions.append(Explosion(self,self.moteur,"assets/images/panda.png"))

        self.physique()

    def fireColision(self):
        AjoutcolisionPanda(self,self.position,self.cage)

    def miseAfire(self):
        # self.moteur.canvas.coords(self.objPanda,-200, 0)
        dicoSon['explosion'].play()
        for u in range(0,self.nbExplosion):
            self.explosions[u].fire(self.position[0],self.position[1]) 

    def physique(self):
        self.position = self.moteur.canvas.coords(self.objPanda)
        self.fireColision()
        self.moteur.canvas.move(self.objPanda,0,0)
        self.moteur.fenetre.after(20,self.physique)